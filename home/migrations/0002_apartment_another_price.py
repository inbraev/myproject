# Generated by Django 3.0.3 on 2020-03-24 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='another_price',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Конвертированная цена'),
        ),
    ]
