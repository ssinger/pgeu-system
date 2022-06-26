# Generated by Django 3.2.11 on 2022-06-26 17:09

from django.db import migrations
import postgresqleu.util.fields


class Migration(migrations.Migration):

    dependencies = [
        ('confreg', '0086_conferenceregistrationlog_changedata'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='photo512',
            field=postgresqleu.util.fields.ImageBinaryField(blank=True, max_length=1000000, null=True, verbose_name='Photo'),
        ),
    ]
