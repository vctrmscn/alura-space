# Generated by Django 5.0.4 on 2024-04-20 23:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_alter_fotografia_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='data_fotografia',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
