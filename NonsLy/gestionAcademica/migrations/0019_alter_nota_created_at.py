# Generated by Django 4.1.3 on 2022-11-28 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionAcademica', '0018_alter_alumno_created_at_alter_alumno_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='created_at',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
