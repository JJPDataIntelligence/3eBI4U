# Generated by Django 2.1.7 on 2019-07-18 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0005_auto_20190717_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerecord',
            name='uid',
            field=models.IntegerField(default=180720191, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicerecord',
            name='LS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_record', to='Cliente.ServiceGround'),
        ),
        migrations.AlterField(
            model_name='servicerecord',
            name='data',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='servicerecord',
            name='description',
            field=models.TextField(verbose_name='Relatório'),
        ),
    ]
