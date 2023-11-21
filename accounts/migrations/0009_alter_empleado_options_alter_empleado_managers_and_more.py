# Generated by Django 4.2.1 on 2023-11-20 03:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0008_alter_empleado_options_alter_empleado_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={},
        ),
        migrations.AlterModelManagers(
            name='empleado',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='email',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='email_empleado',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='password',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='username',
        ),
        migrations.AddField(
            model_name='empleado',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Empleador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empleador', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('contrasena', models.CharField(default='', max_length=100)),
                ('imagen_empleador', models.ImageField(upload_to='uploads/')),
                ('organizacion_empleador', models.CharField(default='', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
