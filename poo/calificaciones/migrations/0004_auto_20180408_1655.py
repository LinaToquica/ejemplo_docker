# Generated by Django 2.0.1 on 2018-04-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calificaciones', '0003_auto_20180408_1653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calificacion',
            old_name='puntaje',
            new_name='max_puntaje',
        ),
        migrations.AddField(
            model_name='calificacion',
            name='min_puntaje',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]