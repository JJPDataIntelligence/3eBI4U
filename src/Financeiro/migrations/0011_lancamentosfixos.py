# Generated by Django 2.1.7 on 2019-04-18 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Financeiro', '0010_auto_20190413_0516'),
    ]

    operations = [
        migrations.CreateModel(
            name='LancamentosFixos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag_receita', models.BooleanField(blank=True, null=True)),
                ('flag_despesa', models.BooleanField(blank=True, null=True)),
                ('valor', models.CharField(max_length=20)),
                ('periodicidade_diaria', models.BooleanField(blank=True, null=True)),
                ('periodicidade_semanal', models.BooleanField(blank=True, null=True)),
                ('periodicidade_quinzenal', models.BooleanField(blank=True, null=True)),
                ('periodicidade_mensal', models.BooleanField(blank=True, null=True)),
                ('periodicidade_trimestral', models.BooleanField(blank=True, null=True)),
                ('periodicidade_semestral', models.BooleanField(blank=True, null=True)),
                ('periodicidade_anual', models.BooleanField(blank=True, null=True)),
                ('data_vencimento_inicial', models.DateField()),
            ],
        ),
    ]