# Generated by Django 2.0.1 on 2018-04-10 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180410_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='personatable',
            name='is_super_admin',
            field=models.BooleanField(default=False),
        ),
    ]
