# Generated by Django 2.0.1 on 2018-04-10 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_personatable_calificacion'),
        ('calificaciones', '0005_auto_20180410_2005'),
        ('lugares', '0011_auto_20180410_2057'),
        ('opiniones', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Opinion',
            new_name='OpinionTable',
        ),
    ]
