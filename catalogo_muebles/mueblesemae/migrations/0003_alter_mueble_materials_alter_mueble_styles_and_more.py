# Generated by Django 4.2 on 2025-01-22 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mueblesemae', '0002_rename_fruniture_cliente_furniture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mueble',
            name='materials',
            field=models.CharField(choices=[('B', 'Bambu'), ('FC', 'Fibras de Coco'), ('E', 'Eco-plasticos'), ('M', 'Madera Sostenible'), ('LO', 'Lino Orgonico'), ('C', 'Corcho')], max_length=30),
        ),
        migrations.AlterField(
            model_name='mueble',
            name='styles',
            field=models.CharField(choices=[('M', 'Minimalista'), ('MU', 'Multifuncionales'), ('I', 'Industrial'), ('S', 'Sostenibles')], max_length=30),
        ),
        migrations.AlterField(
            model_name='mueble',
            name='type',
            field=models.CharField(choices=[('A', 'Organizacion'), ('H', 'Hool/Entrada'), ('B', 'Confort')], max_length=30),
        ),
    ]
