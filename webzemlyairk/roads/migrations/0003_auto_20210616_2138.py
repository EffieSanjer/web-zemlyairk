# Generated by Django 3.2 on 2021-06-16 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roads', '0002_rename_descripion_road_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('show_name', models.CharField(max_length=250, verbose_name='Название для показа')),
                ('type', models.IntegerField(choices=[(1, 'Населенный пункт'), (2, 'Садоводство'), (3, 'Коттеджный поселок'), (4, 'Местность')], verbose_name='Тип')),
                ('distance', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Удаленность')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8, verbose_name='Широта')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=8, verbose_name='Долгота')),
                ('photos', models.JSONField(default='{}', verbose_name='Фотографии')),
                ('date_delete', models.DateField(blank=True, null=True, verbose_name='Дата удаления')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.DeleteModel(
            name='Road',
        ),
        migrations.AddField(
            model_name='family',
            name='child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child', to='roads.locality'),
        ),
        migrations.AddField(
            model_name='family',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='roads.locality'),
        ),
    ]