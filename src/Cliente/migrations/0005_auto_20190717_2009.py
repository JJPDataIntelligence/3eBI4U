# Generated by Django 2.1.7 on 2019-07-17 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0004_auto_20190717_1906'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serviceorder',
            options={'permissions': (('can_view_OSList', 'Grants Permission to OS Listing View'),)},
        ),
    ]
