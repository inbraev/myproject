# Generated by Django 3.0.3 on 2020-04-30 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='house_number',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер дома'),
        ),
    ]
