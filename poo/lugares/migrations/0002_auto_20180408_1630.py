# Generated by Django 2.0.1 on 2018-04-08 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foto_lugar',
            name='lugar',
        ),
        migrations.AddField(
            model_name='ciudad',
            name='departamento',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lugar',
            name='fotos',
            field=models.ManyToManyField(to='lugares.Foto_lugar'),
        ),
        migrations.AlterField(
            model_name='foto_lugar',
            name='foto_path',
            field=models.ImageField(upload_to='static/gallery/'),
        ),
    ]
