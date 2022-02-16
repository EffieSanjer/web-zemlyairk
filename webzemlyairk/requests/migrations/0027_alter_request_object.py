# Generated by Django 3.2 on 2021-06-19 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0003_auto_20210616_2148'),
        ('requests', '0026_auto_20210619_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='object',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='objs', to='objects.object'),
        ),
    ]