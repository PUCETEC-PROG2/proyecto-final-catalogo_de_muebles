# Generated by Django 4.2 on 2025-02-13 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mueblesemae', '0003_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mueble',
            name='type',
        ),
        migrations.AlterField(
            model_name='categoria',
            name='name',
            field=models.CharField(choices=[('O', 'Organizacion'), ('H', 'Hool'), ('C', 'Confort')], max_length=15),
        ),
    ]
