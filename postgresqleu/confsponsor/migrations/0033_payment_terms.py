# Generated by Django 3.2.22 on 2024-11-15 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confsponsor', '0032_sponsorshipbenefit_include_in_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsorshiplevel',
            name='paymentdueby',
            field=models.DateField(blank=True, help_text='The last acceptable due date for payments. If payment terms go beyond this date then the invoice is due at this date', null=True, verbose_name='The latest date the payment is due by'),
        ),
        migrations.RunSQL(
            """
            update confsponsor_sponsorshiplevel set paymentdueby=conf.startdate-'5 days'::interval from confreg_conference conf
            where conf.id = conference_id
            """,
            ""
        ),
        migrations.AlterField(
            model_name='sponsorshiplevel',
            name='paymentdueby',
            field=models.DateField(blank=True, help_text='The last acceptable due date for payments. If payment terms go beyond this date then the invoice is due at this date', null=False, verbose_name='The latest date the payment is due by'),
        ),
        migrations.AddField(
            model_name='sponsorshiplevel',
            name='paymentdays',
            field=models.IntegerField(default=30, null=True, verbose_name='Number of days until payment is due'),
        ),
    ]
