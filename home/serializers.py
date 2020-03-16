from rest_framework import serializers

from .models import *


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'name')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'room')


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = ('id', 'floor')


class ConstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Construction
        fields = ('id', 'name')


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('id', 'name')


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('id', 'name')


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'total_area', 'living_area')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name', 'country')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'region')


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'name', 'city')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'country', 'region', 'city', 'district', 'street', 'house_number', 'latitude', 'longitude')


class Location2Serializer(serializers.ModelSerializer):
    country = serializers.CharField(source='country.__str__')
    region = serializers.CharField(source='region.__str__')
    city = serializers.CharField(source='city.__str__')
    district = serializers.CharField(source='district.__str__')

    class Meta:
        model = Location
        fields = ('id', 'country', 'region', 'city', 'district', 'street', 'house_number', 'latitude', 'longitude')


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ('id', 'furniture', 'heat', 'gas', 'electricity', 'internet', 'phone', 'elevator', 'security',
                  'parking')


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'name')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name')


class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = ('id', 'name')


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id', 'role', 'phone', 'name', 'surname')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'apartment', 'name_of_publication', 'text_of_publication', 'date_of_publication', 'owner')


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, required=False)

    class Meta:
        model = Image
        fields = ('id', 'image', 'apartment')


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'apartment', 'arrival_date', 'departure_date')


class ApartmentSerializer(serializers.ModelSerializer):
    # owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    location = LocationSerializer()
    images = ImageSerializer(many=True)
    area = AreaSerializer()
    contact = ContactSerializer()
    detail = DetailSerializer()
    comments = CommentSerializer(many=True, read_only=True)
    orders = BookingSerializer(many=True, read_only=True)

    class Meta:
        model = Apartment
        fields = ('id', 'type', 'room', 'floor', 'area', 'series', 'construction_type', 'state',
                  'detail', 'location', 'rental_period', 'price', 'currency', 'preview_image', 'description',
                  'pub_date', 'images', 'contact', 'owner', 'comments', 'orders')

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        images_data = validated_data.pop('images')
        area_data = validated_data.pop('area')
        contact_data = validated_data.pop('contact')
        detail_data = validated_data.pop('detail')

        area = Area.objects.create(**area_data)
        location = Location.objects.create(**location_data)
        contact = Contact.objects.create(**contact_data)
        detail = Detail.objects.create(**detail_data)

        apartment = Apartment.objects.create(area=area, location=location, detail=detail, contact=contact, **validated_data)

        for image_data in images_data:
            Image.objects.create(**image_data)
        return apartment


class ApartmentsSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.__str__')
    location = Location2Serializer(many=False)
    images = ImageSerializer(many=True)
    contact = ContactSerializer(many=False)
    type = serializers.CharField(source='type.__str__')
    room = serializers.CharField(source='room.__str__')
    currency = serializers.CharField(source='currency.__str__')
    floor = serializers.CharField(source='floor.__str__')
    series = serializers.CharField(source='series.__str__')
    construction_type = serializers.CharField(source='construction_type.__str__')
    state = serializers.CharField(source='state.__str__')
    rental_period = serializers.CharField(source='rental_period.__str__')
    comments = CommentSerializer(many=True, read_only=True)
    orders = BookingSerializer(many=True, read_only=True)
    detail = DetailSerializer(many=False)
    area = AreaSerializer(many=False)

    class Meta:
        model = Apartment
        fields = ('id', 'type', 'room', 'floor', 'area', 'series', 'construction_type', 'state',
                  'detail', 'location', 'rental_period', 'price', 'currency', 'preview_image', 'description',
                  'pub_date', 'images', 'contact', 'owner', 'comments', 'orders')


class ApartmentsTypeSerializer(serializers.ModelSerializer):
    types = TypeSerializer(many=True)

    class Meta:
        model = Apartment
        fields = ('id', 'types',)


