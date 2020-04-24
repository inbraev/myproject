# Generated by Django 3.0.3 on 2020-04-23 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_apartmentimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='living_area',
            field=models.FloatField(blank=True, null=True, verbose_name='Жилая площадь'),
        ),
        migrations.AlterField(
            model_name='area',
            name='total_area',
            field=models.FloatField(blank=True, null=True, verbose_name='Общая площадь'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='arrival_date',
            field=models.DateField(blank=True, help_text='гггг-мм-дд', null=True, verbose_name='Дата прибытия'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='departure_date',
            field=models.DateField(blank=True, help_text='гггг-мм-дд', null=True, verbose_name='Дата отбытия'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name_of_publication',
            field=models.CharField(blank=True, default=' ', help_text='Введите заголовок', max_length=100, null=True, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text_of_publication',
            field=models.TextField(blank=True, help_text='Введите текст', null=True, verbose_name='Текст публикации'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='location',
            name='house_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер дома'),
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Долгота'),
        ),
    ]