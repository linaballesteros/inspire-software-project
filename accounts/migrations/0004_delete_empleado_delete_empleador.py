# Generated by Django 4.2.1 on 2023-11-19 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_imagen_empleado_imagen_empleado_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Empleado',
        ),
        migrations.DeleteModel(
            name='Empleador',
        ),
    ]