# Generated by Django 4.1.3 on 2022-12-03 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionAcademica', '0037_alter_asignatura_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='curso',
        ),
        migrations.AddField(
            model_name='alumno',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestionAcademica.curso'),
        ),
    ]
