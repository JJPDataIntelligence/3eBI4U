# Generated by Django 2.1.7 on 2019-04-17 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ControleAdministrativo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionarionivel',
            name='cargo_id',
        ),
    ]