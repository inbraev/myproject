from rest_framework import serializers

from .models import *


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'name',)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image',)


class ApartmentsTypeSerializer(serializers.ModelSerializer):
    types = TypeSerializer(many=True)

    class Meta:
        model = Apartment
        fields = ('id', 'types',)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'house_number', 'street', 'city', 'postcode', 'country', 'country_code')


class ApartmentSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Apartment
        fields = (
            'id', 'type', 'room', 'square', 'date_of_arrival', 'date_of_departure', 'price', 'description',
            'status', 'pub_date', 'images', 'owner', 'latitude', 'longitude', 'address')

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        images_data = validated_data.pop('images')

        address = Address.objects.create(**address_data)
        apartment = Apartment.objects.create(address=address, **validated_data)

        for image_data in images_data:
            Image.objects.create(apartment=apartment, **image_data)
        return apartment


class AnnouncementSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='type.__str__')
    address = AddressSerializer(many=False)
    owner = serializers.CharField(source='owner.__str__')
    images = ImageSerializer(many=True)

    class Meta:
        model = Apartment
        fields = ('id', 'type', 'room', 'address', 'square', 'date_of_arrival', 'date_of_departure', 'price', 'description',
                  'status', 'pub_date', 'images', 'owner')
