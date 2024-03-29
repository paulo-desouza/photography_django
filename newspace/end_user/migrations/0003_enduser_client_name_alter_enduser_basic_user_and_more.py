# Generated by Django 5.0 on 2024-01-30 17:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_content_address'),
        ('end_user', '0002_alter_enduser_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='enduser',
            name='client_name',
            field=models.CharField(default='whatever', max_length=50, verbose_name='Nome do seu Cliente'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='enduser',
            name='basic_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AlterField(
            model_name='enduser',
            name='content',
            field=models.ManyToManyField(to='content.content', verbose_name='Conteúdo permitido ao usuário'),
        ),
    ]
