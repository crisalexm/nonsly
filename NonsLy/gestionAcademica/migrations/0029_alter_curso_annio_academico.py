# Generated by Django 4.1.3 on 2022-12-02 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionAcademica', '0028_alter_curso_annio_academico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='annio_academico',
            field=models.CharField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022, max_length=5),
        ),
    ]
