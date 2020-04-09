from rest_framework import serializers

from .models import *


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'type')


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
    owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    apartment = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'apartment', 'name_of_publication', 'text_of_publication', 'date_of_publication', 'owner')


class BookingSerializer(serializers.ModelSerializer):
    apartment = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Booking
        fields = ('id', 'apartment', 'arrival_date', 'departure_date')

    def validate(self, data):
        if data['arrival_date'] > data['departure_date']:
            raise serializers.ValidationError("Дата заезда не может быть позже даты выезда!!!")
        return data


class ApartmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentImage
        fields = ('image',)
class NewApartmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewApartmentImage
        fields = ('image',)


class ApartmentsTypeSerializer(serializers.ModelSerializer):
    types = TypeSerializer(many=True)

    class Meta:
        model = Apartment
        fields = ('id', 'types',)


class ApartmentsRegionSerializer(serializers.ModelSerializer):
    location = RegionSerializer(many=True)

    class Meta:
        model = Apartment
        fields = ('id', 'region')


class RegionsSerializer(serializers.ModelSerializer):
    regions = RegionSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ('id', 'regions',)


class CitiesSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, read_only=True)

    class Meta:
        model = Region
        fields = ('id', 'cities',)


class DistrictsSerializer(serializers.ModelSerializer):
    districts = DistrictSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ('id', 'districts',)


class uploadSerializer(serializers.HyperlinkedModelSerializer):
    images = ApartmentImageSerializer(source='apartment_image', many=True, read_only=True)

    class Meta:
        model = ApartmentImage
        fields = ('images', 'image',)

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        my_view = self.context['view']
        object_id = my_view.kwargs.get('pk')
        apartment = Apartment.objects.get(id=object_id)
        for image_data in images_data.values():
            ApartmentImage.objects.create(apartment=apartment, image=image_data)
        apartment.save()
        return apartment

class NewUploadSerializer(serializers.HyperlinkedModelSerializer):
    images = NewApartmentImageSerializer(source='apartment_image', many=True, read_only=True)

    class Meta:
        model = NewApartmentImage
        fields = ('images', 'image',)

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        my_view = self.context['view']
        object_id = my_view.kwargs.get('pk')
        apartment = NewApartment.objects.get(id=object_id)
        for image_data in images_data.values():
            NewApartmentImage.objects.create(apartment=apartment, image=image_data)
        apartment.save()
        return apartment


class ApartmentSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    location = LocationSerializer()
    apartment_image = uploadSerializer(many=True, read_only=True)
    area = AreaSerializer()
    contact = ContactSerializer()
    detail = DetailSerializer()
    comments = CommentSerializer(many=True, read_only=True)
    orders = BookingSerializer(many=True, read_only=True)

    class Meta:
        model = Apartment
        fields = ('id', 'type', 'room', 'floor', 'area', 'series', 'construction_type', 'state',
                  'detail', 'location', 'rental_period', 'price', 'currency', 'another_price', 'preview_image',
                  'description',
                  'pub_date', 'apartment_image', 'contact', 'owner', 'comments', 'orders')

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        area_data = validated_data.pop('area')
        contact_data = validated_data.pop('contact')
        detail_data = validated_data.pop('detail')
        area = Area.objects.create(**area_data)
        location = Location.objects.create(**location_data)
        contact = Contact.objects.create(**contact_data)
        detail = Detail.objects.create(**detail_data)
        apartment = Apartment.objects.create(area=area, location=location, detail=detail, contact=contact,
                                             **validated_data)
        return apartment


class NewApartmentSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    apartment_image = NewUploadSerializer(many=True, read_only=True)
    contact = ContactSerializer()
    comments = CommentSerializer(many=True, read_only=True)
    orders = BookingSerializer(many=True, read_only=True)

    class Meta:
        model = NewApartment
        fields = ('id', 'type', 'room', 'floor', 'area', 'series', 'construction_type', 'state',
                   'location', 'price', 'currency', 'another_price', 'preview_image',
                  'description', 'title', 'furniture', 'heat', 'gas', 'electricity', 'internet', 'phone',
                  'parking', 'elevator', 'security',
                  'pub_date', 'apartment_image', 'contact', 'owner', 'comments', 'orders')

    def create(self, validated_data):
        contact_data = validated_data.pop('contact')
        contact = Contact.objects.create(**contact_data)
        apartment = Apartment.objects.create( contact=contact,
                                             **validated_data)
        return apartment


class ApartmentsSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.__str__')
    location = Location2Serializer(many=False)
    apartment_image = uploadSerializer(many=True, read_only=True)
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
                  'detail', 'location', 'rental_period', 'price', 'currency', 'another_price', 'preview_image',
                  'description',
                  'pub_date', 'apartment_image', 'contact', 'owner', 'comments', 'orders')


class NewApartmentsSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.__str__')

    apartment_image = NewUploadSerializer(many=True, read_only=True)
    contact = ContactSerializer(many=False)
    type = serializers.CharField(source='type.__str__')

    currency = serializers.CharField(source='currency.__str__')

    series = serializers.CharField(source='series.__str__')
    construction_type = serializers.CharField(source='construction_type.__str__')
    state = serializers.CharField(source='state.__str__')

    comments = CommentSerializer(many=True, read_only=True)
    orders = BookingSerializer(many=True, read_only=True)



    class Meta:
        model = NewApartment
        fields = ('id', 'type', 'room', 'floor', 'area', 'series', 'construction_type', 'state',
                'location',   'price', 'currency', 'another_price', 'preview_image',
                  'description','title','furniture', 'heat', 'gas', 'electricity', 'internet', 'phone',
                  'parking', 'elevator', 'security',
                  'pub_date', 'apartment_image', 'contact', 'owner', 'comments', 'orders')
