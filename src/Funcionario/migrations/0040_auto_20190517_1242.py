# Generated by Django 2.1.7 on 2019-05-17 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Funcionario', '0039_auto_20190517_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anotherjobinfo',
            name='vinc_outra_emp_salario',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='interninfo',
            name='estag_valor_bolsa',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]