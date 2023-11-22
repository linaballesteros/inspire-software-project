# Generated by Django 4.2.4 on 2023-11-21 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0010_alter_empleado_user'),
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insignia',
            fields=[
                ('insignia_id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Habilidades', models.CharField(max_length=200)),
                ('Imagen', models.ImageField(upload_to='')),
                ('Emisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.empleador', verbose_name='ID Emisor')),
                ('Reto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenges.reto', verbose_name='ID Reto')),
            ],
        ),
        migrations.CreateModel(
            name='Recibir_insignia',
            fields=[
                ('assertion_id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('empleado_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.empleado', verbose_name='ID empleado')),
                ('insignia_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badges.insignia', verbose_name='ID Insignia Otorgada')),
            ],
        ),
    ]
