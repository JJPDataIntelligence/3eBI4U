# Generated by Django 2.1.7 on 2019-07-22 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0015_auto_20190722_1630'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='occurrencecall',
            options={'permissions': (('occurrence_listing_viewer', 'Grants Permission to Occurrence Listing View'),)},
        ),
    ]
