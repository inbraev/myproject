from rest_framework import serializers
from .models import *


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'name')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = (
            'type', 'room', 'square', 'date_of_arrival', 'date_of_departure', 'price', 'description',
            'status', 'pub_date', 'image', 'owner')


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ('type', 'room', 'square', 'date_of_arrival', 'date_of_departure', 'price', 'description',
            'status', 'pub_date', 'image', 'owner', 'latitude', 'longitude')


class ApartmentsTypeSerializer(serializers.ModelSerializer):
    types = TypeSerializer(many=True)

    class Meta:
        model = Apartment
        fields = ('types',)

