# Generated by Django 4.2.6 on 2023-11-11 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recompensa', '0003_logo_remove_recompensa_description_recompensa_tokens_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='logo',
        ),
        migrations.AlterField(
            model_name='recompensa',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='recompensa',
            name='tokens',
            field=models.IntegerField(),
        ),
    ]
