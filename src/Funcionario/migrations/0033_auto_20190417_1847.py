# Generated by Django 2.1.7 on 2019-04-17 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Funcionario', '0032_auto_20190417_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positioninfo',
            name='funcao_nivel',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]