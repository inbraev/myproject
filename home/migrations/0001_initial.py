# Generated by Django 3.0.2 on 2020-03-03 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('preview_image', models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name='Главное фото')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Объект недвижимости',
                'verbose_name_plural': 'Объекты недвижимости',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_area', models.FloatField(verbose_name='Общая площадь')),
                ('living_area', models.FloatField(verbose_name='Жилая площадь')),
            ],
            options={
                'verbose_name': 'Площадь',
                'verbose_name_plural': 'Площадь',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Construction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Тип постройки')),
            ],
            options={
                'verbose_name': 'Тип постройки',
                'verbose_name_plural': 'Типы постройки',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Валюта')),
            ],
            options={
                'verbose_name': 'Валюта',
                'verbose_name_plural': 'Валюты',
            },
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('furniture', models.BooleanField(verbose_name='Мебель')),
                ('heat', models.BooleanField(verbose_name='Отопление')),
                ('gas', models.BooleanField(verbose_name='Газ')),
                ('electricity', models.BooleanField(verbose_name='Электричество')),
                ('internet', models.BooleanField(verbose_name='Интернет')),
                ('phone', models.BooleanField(verbose_name='Телевонная линия')),
                ('parking', models.BooleanField(blank=True, null=True, verbose_name='Парковка')),
                ('elevator', models.BooleanField(blank=True, null=True, verbose_name='Лифт')),
                ('security', models.BooleanField(blank=True, null=True, verbose_name='Охрана')),
            ],
            options={
                'verbose_name': 'Характеристика',
                'verbose_name_plural': 'Характеристики',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Район')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.City', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.IntegerField(verbose_name='Этаж')),
            ],
            options={
                'verbose_name': 'Этаж',
                'verbose_name_plural': 'Этажи',
            },
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Период аренды')),
            ],
            options={
                'verbose_name': 'Период аренды',
                'verbose_name_plural': 'Периоды аренды',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Тип арендодатора')),
            ],
            options={
                'verbose_name': 'Тип арендотатора',
                'verbose_name_plural': 'Типы арендодатора',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=100, verbose_name='Количество комнат')),
            ],
            options={
                'verbose_name': 'Комната',
                'verbose_name_plural': 'Комнаты',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Серия')),
            ],
            options={
                'verbose_name': 'Серия',
                'verbose_name_plural': 'Серии',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Состояние')),
            ],
            options={
                'verbose_name': 'Состояние',
                'verbose_name_plural': 'Состояния',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Тип недвижимости',
                'verbose_name_plural': 'Типы недвижимости',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Регион')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Country', verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Регион',
                'verbose_name_plural': 'Регионы',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('house_number', models.IntegerField(verbose_name='Номер дома')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.City', verbose_name='Город')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Country', verbose_name='Страна')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.District', verbose_name='Район')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Region', verbose_name='Регион')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('apartment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='home.Apartment', verbose_name='Объект недвижимости')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=13, verbose_name='Номер телефона')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, max_length=30, null=True, verbose_name='Фамилия')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Role', verbose_name='Тип арендодатора')),
            ],
            options={
                'verbose_name': 'Контактные данные',
                'verbose_name_plural': 'Контактные данные',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_publication', models.CharField(default=' ', help_text='Введите заголовок', max_length=100, verbose_name='Заголовок')),
                ('text_of_publication', models.TextField(help_text='Введите текст', verbose_name='Текст публикации')),
                ('date_of_publication', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('apartment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='home.Apartment', verbose_name='Объект недвижимости')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Region', verbose_name='Регион'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_date', models.DateField(help_text='гггг-мм-дд', verbose_name='Дата прибытия')),
                ('departure_date', models.DateField(help_text='гггг-мм-дд', verbose_name='Дата отбытия')),
                ('apartment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='home.Apartment', verbose_name='Объект недвижимости')),
            ],
            options={
                'verbose_name': 'Система бронирования',
                'verbose_name_plural': 'Система бронирования',
            },
        ),
        migrations.AddField(
            model_name='apartment',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='area', to='home.Area', verbose_name='Площадь'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='construction_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Construction', verbose_name='Тип сторения'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contact', to='home.Contact', verbose_name='Контактиные данные'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Currency', verbose_name='Валюта'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='detail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='detail', to='home.Detail', verbose_name='Характеристики'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='floor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Floor', verbose_name='Этаж'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='location', to='home.Location', verbose_name='Расположение'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='rental_period',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Rent', verbose_name='Период аренды'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Room', verbose_name='Количество комнат'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Series', verbose_name='Серия'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.State', verbose_name='Состояние'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Type', verbose_name='Тип недвижимости'),
        ),
    ]
