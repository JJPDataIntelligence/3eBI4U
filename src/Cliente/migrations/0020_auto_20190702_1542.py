# Generated by Django 2.1.7 on 2019-07-02 18:42

import Cliente.utilities
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0019_auto_20190621_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicinfo',
            name='numero_documento_CNPJ',
        ),
        migrations.RemoveField(
            model_name='basicinfo',
            name='numero_documento_CPF',
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='numero_documento',
            field=models.CharField(blank=True, max_length=18, null=True, validators=[Cliente.utilities.validateCPFCNPJ], verbose_name='Número do Documento'),
        ),
        migrations.AlterField(
            model_name='servicedescription',
            name='funcionario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='descricao_servico_funcionario', to='Funcionario.BasicInfo'),
            preserve_default=False,
        ),
    ]