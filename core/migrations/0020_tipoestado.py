# Generated by Django 3.1.2 on 2023-06-24 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20230624_0111'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoEstado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
    ]