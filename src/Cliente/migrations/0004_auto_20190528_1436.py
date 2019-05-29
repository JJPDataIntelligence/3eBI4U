# Generated by Django 2.1.7 on 2019-05-28 17:36

import Cliente.utilities
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0003_auto_20190527_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicinfo',
            name='numero_documento_CNPJ',
            field=models.CharField(blank=True, max_length=18, null=True, validators=[Cliente.utilities.validateCNPJ]),
        ),
    ]
