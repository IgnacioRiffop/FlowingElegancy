# Generated by Django 3.1.2 on 2023-06-24 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_tipoestado'),
    ]

    operations = [
        migrations.AddField(
            model_name='compras',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.tipoestado'),
            preserve_default=False,
        ),
    ]