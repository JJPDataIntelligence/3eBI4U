# Generated by Django 2.1.7 on 2019-05-29 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Funcionario', '0041_auto_20190529_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicinfo',
            name='afastamento',
            field=models.BooleanField(default=False),
        ),
    ]
