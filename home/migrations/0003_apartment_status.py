# Generated by Django 3.0.3 on 2020-03-26 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_apartment_another_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Статус объекта недвижимости'),
        ),
    ]
