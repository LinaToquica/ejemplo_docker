# Generated by Django 2.0.1 on 2018-04-10 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('opiniones', '0001_initial'),
        ('lugares', '0008_auto_20180408_2341'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lugar',
            new_name='LugarTable',
        ),
    ]