# Generated by Django 2.1.7 on 2019-05-10 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Financeiro', '0021_auto_20190509_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='identificador_receita',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='saida',
            name='identificador_despesa',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entrada',
            name='observacao',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
