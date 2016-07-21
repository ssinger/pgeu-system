#
# This script compares the balance on the paypal account with the one
# in the accounting system, raising an alert if they are different
# (which indicates that something has been incorrectly processed).
#
# Copyright (C) 2010-2016, PostgreSQL Europe
#


from django.core.management.base import BaseCommand, CommandError
from django.db import connection, transaction
from django.conf import settings

from postgresqleu.paypal.util import PaypalAPI
from postgresqleu.mailqueue.util import send_simple_mail

class Command(BaseCommand):
	help = 'Compare paypal balance to the accounting system'

	@transaction.atomic
	def handle(self, *args, **options):
		api = PaypalAPI()

		# We only ever care about the primary currency
		paypal_balance = api.get_primary_balance()

		cursor = connection.cursor()
		cursor.execute("SELECT year FROM accounting_year WHERE isopen")
		year = cursor.fetchall()[0][0]

		cursor.execute("SELECT sum(amount)+(SELECT amount FROM accounting_incomingbalance WHERE year_id=%(year)s AND account_id=%(account)s) FROM accounting_journalitem ji INNER JOIN accounting_journalentry je ON ji.journal_id=je.id WHERE je.year_id=%(year)s AND ji.account_id=%(account)s", {
			'account': settings.ACCOUNTING_PAYPAL_INCOME_ACCOUNT,
			'year': year,
		})

		accounting_balance = cursor.fetchall()[0][0]

		if accounting_balance != paypal_balance:
			send_simple_mail(settings.INVOICE_SENDER_EMAIL,
							 settings.PAYPAL_REPORT_RECEIVER,
							 'Paypal balance mismatch!',
							 """Paypal balance ({0}) does not match the accounting system ({1})!

This could be because some entry has been missed in the accouting
(automatic or manual), or because of an ongoing booking of something
that the system deosn't know about.

Better go check manually!
""".format(paypal_balance, accounting_balance))
