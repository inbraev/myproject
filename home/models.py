from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings


class Type(models.Model):
    name = models.CharField('Тип', max_length=100)

    class Meta:
        verbose_name = 'Тип недвижимости'
        verbose_name_plural = 'Типы недвижимости'

    def __str__(self):
        return self.name


ROOM_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4+', '4+'),
    ('', 'Any'),
]


class Image(models.Model):
    image = models.ImageField(upload_to='photos/')

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Address(models.Model):
    house_number=models.IntegerField('Номер дома')
    street = models.CharField('Улица', max_length=100)
    city = models.CharField('Город', max_length=100)
    postcode = models.CharField('Почтовый индекс', max_length=10)
    country = models.CharField('Страна', max_length=20)
    country_code = models.CharField('Код страны', max_length=5)


class Apartment(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='Тип недвижимости')
    room = models.CharField('Количество комнат', max_length=10, choices=ROOM_CHOICES)
    price = models.IntegerField('Цена')
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name='Адрес', default=True)
    square = models.FloatField('Площадь')
    image = models.ManyToManyField(Image, verbose_name='Фотографии', default=True)
    date_of_arrival = models.DateField('Дата прибытия', help_text='гггг-мм-дд')
    date_of_departure = models.DateField('Дата отбытия', help_text='гггг-мм-дд')
    description = models.TextField('Описание')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    status = models.BooleanField('Свободно ли?')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Владелец')

    class Meta:
        verbose_name = 'Объект недвижимости'
        verbose_name_plural = 'Объекты недвижимости'

    def __str__(self):
        return f'{self.type} , {self.room}'
