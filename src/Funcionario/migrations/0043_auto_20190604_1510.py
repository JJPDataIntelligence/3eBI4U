# Generated by Django 2.1.7 on 2019-06-04 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Funcionario', '0042_basicinfo_afastamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicinfo',
            name='primeiro_nome',
            field=models.CharField(default='John Doe', max_length=100),
            preserve_default=False,
        ),
    ]
