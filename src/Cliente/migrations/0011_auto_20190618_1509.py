# Generated by Django 2.1.7 on 2019-06-18 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Funcionario', '0055_auto_20190618_1509'),
        ('Cliente', '0010_auto_20190613_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceDescription',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('qtd_horas', models.IntegerField(blank=True, null=True)),
                ('valor_hora', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('valor_total', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('funcionario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='service_description', to='Funcionario.BasicInfo')),
            ],
        ),
        migrations.RenameField(
            model_name='serviceorder',
            old_name='produto',
            new_name='faturado',
        ),
        migrations.RenameField(
            model_name='serviceorder',
            old_name='servico',
            new_name='servico_produto',
        ),
        migrations.RemoveField(
            model_name='serviceground',
            name='pais',
        ),
        migrations.AddField(
            model_name='serviceorder',
            name='subcategoria',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
