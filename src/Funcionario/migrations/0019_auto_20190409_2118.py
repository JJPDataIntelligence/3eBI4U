# Generated by Django 2.1.7 on 2019-04-10 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Funcionario', '0018_auto_20190409_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankinginfo',
            name='banco_tipo_conta',
            field=models.CharField(blank=True, choices=[('Corrente', 'C. Corrente'), ('Poupança', 'Poupança')], max_length=200, null=True),
        ),
    ]
