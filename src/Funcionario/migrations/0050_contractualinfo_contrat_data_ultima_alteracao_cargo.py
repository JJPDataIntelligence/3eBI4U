# Generated by Django 2.1.7 on 2019-06-06 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Funcionario', '0049_contractualinfo_contrat_funcao_nivel_inicial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractualinfo',
            name='contrat_data_ultima_alteracao_cargo',
            field=models.DateField(blank=True, null=True),
        ),
    ]