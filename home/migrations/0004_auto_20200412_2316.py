# Generated by Django 3.0.3 on 2020-04-12 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200412_0301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newapartmentimage',
            name='apartment',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='rental_period',
        ),
        migrations.DeleteModel(
            name='NewApartment',
        ),
        migrations.DeleteModel(
            name='NewApartmentImage',
        ),
        migrations.DeleteModel(
            name='Rent',
        ),
    ]