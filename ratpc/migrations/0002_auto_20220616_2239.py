# Generated by Django 2.2.28 on 2022-06-16 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratpc', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Libro',
        ),
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'ordering': ['id_vehiculo']},
        ),
    ]
