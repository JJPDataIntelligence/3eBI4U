# Generated by Django 2.1.7 on 2019-07-22 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0013_auto_20190722_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='occurrencecall',
            name='occurrence',
        ),
    ]