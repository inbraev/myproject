# Generated by Django 3.0.3 on 2020-04-06 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200402_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskimage',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taskssssssssss', to='home.Apartment'),
        ),
    ]
