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
            field=models.DateField(blank=True, help_text='The last acceptable due date for payments. If payment terms go behond this date then the invoice is due at this date', null=True, verbose_name='The date the payment is due by'),
        ),
        migrations.AddField(
            model_name='sponsorshiplevel',
            name='paymentterms',
            field=models.IntegerField(default=30, null=True, verbose_name='Number of days until payment is due'),
        ),
    ]
