# Generated by Django 2.1.7 on 2019-04-30 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Financeiro', '0016_auto_20190430_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='classificacao_receita',
        ),
        migrations.RemoveField(
            model_name='entrada',
            name='produto',
        ),
        migrations.RemoveField(
            model_name='entrada',
            name='quantidade_produto',
        ),
    ]