# Generated by Django 3.1.2 on 2023-06-29 02:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20230628_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='suscripcion',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
