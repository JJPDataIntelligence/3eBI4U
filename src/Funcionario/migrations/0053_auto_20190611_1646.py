# Generated by Django 2.1.7 on 2019-06-11 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Funcionario', '0052_auto_20190611_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankinginfo',
            name='basicinfo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='banking_info', to='Funcionario.BasicInfo'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='basicinfo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='contact_info', serialize=False, to='Funcionario.BasicInfo'),
        ),
    ]