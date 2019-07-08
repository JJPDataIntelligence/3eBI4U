# Generated by Django 2.1.7 on 2019-06-13 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0006_auto_20190607_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicinfo',
            name='nome_local_servico',
        ),
        migrations.AlterField(
            model_name='addressinfo',
            name='basicinfo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='address_info', serialize=False, to='Cliente.BasicInfo'),
        ),
        migrations.AlterField(
            model_name='contractualinfo',
            name='basicinfo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='contractual_info', serialize=False, to='Cliente.BasicInfo'),
        ),
    ]