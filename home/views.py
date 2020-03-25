from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from .permissions import IsOwner
from .serializers import *
from rest_framework.exceptions import PermissionDenied, NotFound
from django_filters import rest_framework as filters

class TypeView(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = (permissions.IsAdminUser,)


class RoomView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (permissions.IsAdminUser,)


class FloorView(generics.ListCreateAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
    permission_classes = (permissions.IsAdminUser,)


class ConstructionView(generics.ListCreateAPIView):
    queryset = Construction.objects.all()
    serializer_class = ConstructionSerializer
    permission_classes = (permissions.IsAdminUser,)


class SeriesView(generics.ListCreateAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = (permissions.IsAdminUser,)


class StateView(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = (permissions.IsAdminUser,)


class AreaView(generics.CreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = (permissions.AllowAny,)


class CountryView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (permissions.IsAdminUser,)


class RegionView(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = (permissions.IsAdminUser,)


class CityView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (permissions.IsAdminUser,)


class DistrictView(generics.ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = (permissions.IsAdminUser,)


class LocationView(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (permissions.AllowAny,)


class DetailView(generics.CreateAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
    permission_classes = (permissions.AllowAny,)


class CurrencyView(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = (permissions.IsAdminUser,)


class RoleView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (permissions.IsAdminUser,)


class RentView(generics.ListCreateAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    permission_classes = (permissions.IsAdminUser,)


class ContactView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (permissions.AllowAny,)


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.AllowAny,)
    
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            return serializer.save(owner=self.request.user)
        else:
            raise PermissionDenied('Авторизуйтесь в системе для добавления комментариев')


class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ImageView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (permissions.AllowAny,)


class ApartmentView(generics.CreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ApartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = (permissions.AllowAny,)

    
class ApartmentFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    arrival_date = filters.DateFilter(field_name='orders__arrival_date', lookup_expr='gte')
    departure_date = filters.DateFilter(field_name='orders__departure_date', lookup_expr='lte')
    min_area = filters.NumberFilter(field_name='area__total_area', lookup_expr='gte')
    max_area = filters.NumberFilter(field_name='area__total_area', lookup_expr='lte')

    class Meta:
        model = Apartment
        fields = ['location__region', 'location__city', 'location__district', 'type', 'room', 'floor',
                  'construction_type', 'state',
                  'min_price', 'max_price', 'currency', 'arrival_date', 'departure_date', 'min_area', 'max_area',
                  'rental_period', 'detail__internet', 'detail__furniture', 'detail__heat', 'detail__gas',
                  'detail__phone', 'detail__parking', 'detail__elevator', 'detail__security']
        
        
class ApartmentListView(generics.ListAPIView):
    serializer_class = ApartmentsSerializer
    queryset = Apartment.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ApartmentFilter
    permission_classes = (permissions.AllowAny,)


class ApartmentsTypeView(generics.RetrieveAPIView):
    model = Type
    queryset = Type.objects.all()
    permission_classes = (permissions.AllowAny,)
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        types = Apartment.objects.filter(type_id=instance.id)
        serializer = ApartmentSerializer(types, many=True)
        return Response(serializer.data)
    
    
class RegionsView(generics.RetrieveAPIView):
    model = Country
    queryset = Country.objects.all()
    permission_classes = (permissions.AllowAny,)
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        regions = Region.objects.filter(country_id=instance.id)
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data)


class CitiesView(generics.RetrieveAPIView):
    model = Region
    queryset = Region.objects.all()
    permission_classes = (permissions.AllowAny,)
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        cities = City.objects.filter(region_id=instance.id)
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)


class DistrictsView(generics.RetrieveAPIView):
    model = City
    queryset = City.objects.all()
    permission_classes = (permissions.AllowAny,)
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        districts = District.objects.filter(city_id=instance.id)
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data)


class ApartmentsRegionView(generics.RetrieveAPIView):
    queryset = Region.objects.all()
    permission_classes = (permissions.AllowAny,)
    lookup_field = "pk"
    serializer_class = ApartmentsRegionSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        regions = Apartment.objects.filter(location__region_id=instance.id)
        serializer = ApartmentSerializer(regions, many=True)
        return Response(serializer.data)
    

class OwnerView(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        user = self.request.user
        return Apartment.objects.filter(owner=user)


class OwnerBookingDetail(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def perform_create(self, serializer):
        user = self.request.user
        try:
            apartments = Apartment.objects.get(id=self.kwargs['pk'])
            if user == apartments.owner:
                serializer.save(apartment=apartments)
            else:
                raise PermissionDenied('У вас нету прав на изменение ')
        except:
            raise NotFound('Квартира не найдена')

    def get_queryset(self):
        user = self.request.user
        pk = self.kwargs['pk']
        try:
            apartment = Apartment.objects.get(id=pk)
            if user==apartment.owner:
                return Booking.objects.filter(apartment__id=pk)
            else:
                raise PermissionDenied('У вас нету прав на изменение ')
        except:
            raise NotFound('Квартира не найдена')
