# Generated by Django 4.1.2 on 2022-11-23 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('mesas', 'MESAS'), ('sofas', 'SOFAS'), ('Roupeiro', 'ROUPEIRO')], max_length=20),
        ),
        migrations.AlterField(
            model_name='servico',
            name='tipo',
            field=models.CharField(choices=[('instal', 'INSTALAÇAO'), ('entrega', 'ENTREGA'), ('manut', 'MANUTENÇAO')], max_length=20),
        ),
    ]
