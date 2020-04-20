from datetime import date

from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied, NotFound

from .permissions import IsOwner
from .serializers import *


class TypeView(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = (permissions.AllowAny,)


class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (permissions.AllowAny,)


class FloorView(generics.ListAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
    permission_classes = (permissions.AllowAny,)


class ConstructionView(generics.ListAPIView):
    queryset = Construction.objects.all()
    serializer_class = ConstructionSerializer
    permission_classes = (permissions.AllowAny,)


class SeriesView(generics.ListAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = (permissions.AllowAny,)


class StateView(generics.ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = (permissions.AllowAny,)


class CountryView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (permissions.AllowAny,)


class RegionView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = (permissions.AllowAny,)


class CityView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (permissions.AllowAny,)


class DistrictView(generics.ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = (permissions.AllowAny,)


class AreaView(generics.CreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = (permissions.AllowAny,)


class CurrencyView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = (permissions.AllowAny,)


class LocationView(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (permissions.AllowAny,)


class DetailView(generics.CreateAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
    permission_classes = (permissions.AllowAny,)


class RoleView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (permissions.AllowAny,)


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


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAdminUser,)


class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ApartmentView(generics.CreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

class ApartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = (IsOwner,)
    
    
class ApartmentDetail(generics.RetrieveAPIView):
    queryset = Apartment.objects.all()
    serializer_class = PrettyApartmentSerializer
    permission_classes = (permissions.AllowAny,)



class ApartmentFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    arrival_date = filters.DateFilter(field_name='orders__departure_date', lookup_expr='gt')
    departure_date = filters.DateFilter(field_name='orders__arrival_date', lookup_expr='lt')
    min_area = filters.NumberFilter(field_name='area__total_area', lookup_expr='gte')
    max_area = filters.NumberFilter(field_name='area__total_area', lookup_expr='lte')

    class Meta:
        model = Apartment
        fields = ['location__region', 'location__city', 'location__district', 'type', 'room', 'floor',
                  'construction_type', 'state',
                  'min_price', 'max_price', 'currency', 'arrival_date', 'departure_date', 'min_area', 'max_area',
                  'detail__internet', 'detail__furniture', 'detail__heat', 'detail__gas',
                  'detail__phone', 'detail__parking', 'detail__elevator', 'detail__security']


class ApartmentListView(generics.ListAPIView):
    serializer_class = ApartmentsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ApartmentFilter
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        for apartment in Apartment.objects.all():
            if apartment.orders:
                for order in apartment.orders.filter(departure_date__gte=date.today()):
                    if date.today() == order.arrival_date:
                        apartment.status = False
                        apartment.save()
                    if date.today() == order.departure_date:
                        apartment.status = True
                        apartment.save()
        return Apartment.objects.filter(status=True)


class CreateComment(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Comment.objects.filter(apartment_id=self.kwargs["pk"])
        return queryset

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            try:
                apartments = Apartment.objects.get(id=self.kwargs['pk'])
                return serializer.save(owner=self.request.user, apartment=apartments)
            except:
                raise PermissionDenied("Квартира не найдена")
        else:
            raise PermissionDenied('Авторизуйтесь в системе для добавления комментариев')

    serializer_class = CommentSerializer
    permission_classes = (permissions.AllowAny,)


class OwnerView(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        try:
            user = self.request.user
            return Apartment.objects.filter(owner=user)
        except:
            raise PermissionDenied('Вы не являетесь собственником квартиры')


class CreateBooking(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (IsOwner,)

    def perform_create(self, serializer):
        try:
            apartments = Apartment.objects.get(id=self.kwargs['id'])
            if self.request.user == apartments.owner:
                serializer.save(apartment=apartments)
            else:
                raise PermissionDenied('Вы не являетесь собственником квартиры')
        except:
            raise NotFound('Квартира не найдена')

    def get_queryset(self):
        try:
            apartment = Apartment.objects.get(id=self.kwargs['id'])
            if self.request.user == apartment.owner:
                return Booking.objects.filter(apartment__id=self.kwargs['id'])
            else:
                raise PermissionDenied('У вас нету прав на изменение ')
        except:
            raise NotFound('Квартира не найдена')


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class UploadImage(generics.ListCreateAPIView):
    serializer_class = uploadSerializer
    queryset = Apartment.objects.all()
