# Generated by Django 2.1.7 on 2019-04-12 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0001_initial'),
        ('Financeiro', '0002_auto_20190412_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='Cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Cliente.BasicInfo'),
            preserve_default=False,
        ),
    ]