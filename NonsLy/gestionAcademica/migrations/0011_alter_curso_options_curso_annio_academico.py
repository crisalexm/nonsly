# Generated by Django 4.1.3 on 2022-11-27 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionAcademica', '0010_nota'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curso',
            options={'ordering': ['nivel'], 'verbose_name_plural': 'Cursos'},
        )
    ]
