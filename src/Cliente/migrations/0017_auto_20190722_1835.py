# Generated by Django 2.1.7 on 2019-07-22 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0016_auto_20190722_1827'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='occurrencecall',
            options={'permissions': (('occurrence_listing_viewer', 'Grants Permission to Occurrence Listing View'), ('occurrence_manage', 'Grants Permission to manage Occurrence Calls'))},
        ),
    ]
