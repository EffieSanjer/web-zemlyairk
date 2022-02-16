# Generated by Django 3.2 on 2021-06-12 07:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0020_alter_request_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='date_add',
            field=models.DateField(default=datetime.date(2021, 6, 12), verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='request',
            name='date_start',
            field=models.DateField(default=datetime.date(2021, 6, 12), verbose_name='Дата начала'),
        ),
    ]