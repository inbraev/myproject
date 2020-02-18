# Generated by Django 3.0.2 on 2020-02-17 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yourthome', '0006_auto_20200217_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='image',
            field=models.ManyToManyField(blank=True, null=True, to='yourthome.Image', verbose_name='Фотографии'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='room',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4+', '4+')], max_length=10, verbose_name='Количество комнат'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
