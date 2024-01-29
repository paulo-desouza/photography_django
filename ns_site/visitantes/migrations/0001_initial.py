# Generated by Django 5.0.1 on 2024-01-20 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('porteiros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=194, verbose_name='Nome Completo')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('numero_casa', models.PositiveSmallIntegerField(verbose_name='Numero da casa a ser visitada')),
                ('placa_veiculo', models.CharField(blank=True, max_length=7, null=True, verbose_name='Placa de Veiculo')),
                ('horario_chegada', models.DateTimeField(auto_now_add=True, verbose_name='Horario de chegada na portaria')),
                ('horario_saida', models.DateTimeField(blank=True, null=True, verbose_name='Horario de saida do condominio')),
                ('horario_autorizacao', models.DateTimeField(blank=True, null=True, verbose_name='Horario de autorizacao de entrada')),
                ('morador_responsavel', models.CharField(blank=True, max_length=194, verbose_name='Nome do morador responsavel por autorizar a entrada do visitante')),
                ('registrado_por', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='porteiros.porteiro', verbose_name='Porteiro responsavel pelo Registro')),
            ],
            options={
                'verbose_name': 'Visitante',
                'verbose_name_plural': 'Visitantes',
                'db_table': 'visitante',
            },
        ),
    ]