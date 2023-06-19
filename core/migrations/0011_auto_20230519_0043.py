# Generated by Django 3.1.2 on 2023-05-19 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20230518_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='producto',
        ),
        migrations.AddField(
            model_name='carrito',
            name='producto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.producto'),
            preserve_default=False,
        ),
    ]