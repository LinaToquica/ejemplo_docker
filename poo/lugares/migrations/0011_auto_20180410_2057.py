# Generated by Django 2.0.1 on 2018-04-10 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calificaciones', '0005_auto_20180410_2005'),
        ('lugares', '0010_lugartable_es_lugar_aprobado'),
    ]

    operations = [
        migrations.AddField(
            model_name='lugartable',
            name='calificacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='calificaciones.CalificacionTable'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lugartable',
            name='puntaje',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
