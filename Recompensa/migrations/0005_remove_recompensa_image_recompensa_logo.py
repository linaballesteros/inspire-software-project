# Generated by Django 4.2.6 on 2023-11-11 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recompensa', '0004_delete_logo_alter_recompensa_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recompensa',
            name='image',
        ),
        migrations.AddField(
            model_name='recompensa',
            name='logo',
            field=models.CharField(default='', max_length=100),
        ),
    ]
