# Generated by Django 4.2.6 on 2023-11-06 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recompensa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recompensa',
            name='url',
        ),
    ]
