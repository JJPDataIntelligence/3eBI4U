# Generated by Django 2.1.7 on 2019-06-18 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Funcionario', '0055_auto_20190618_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependente',
            name='basicinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dependente', to='Funcionario.BasicInfo'),
        ),
    ]
