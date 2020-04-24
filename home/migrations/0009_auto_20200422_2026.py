# Generated by Django 3.0.3 on 2020-04-22 14:26

import django.contrib.postgres.fields
from django.db import migrations, models



class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('home', '0008_auto_20200418_0313'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apartmentimage',
            options={'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AddField(
            model_name='apartment',
            name='storey',
            field=models.PositiveSmallIntegerField(default=9, verbose_name='Этажность'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='nearby_objects',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=250, null=True), blank=True, default=list, null=True, size=None, verbose_name='Рядом есть'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='objects_in_apartment',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=250, null=True), blank=True, default=list, null=True, size=None, verbose_name='В квартире есть'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='apartmentimage',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Фотография'),
        ),
    ]
