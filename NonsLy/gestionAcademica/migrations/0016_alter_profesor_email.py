# Generated by Django 4.1.3 on 2022-11-27 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionAcademica', '0015_rename_fechanacimiento_profesor_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]
