from datetime import date

from django.http import Http404
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
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


class ApartmentDetail(APIView):

    def get_object(self, pk):
        try:
            return Apartment.objects.get(pk=pk)
        except:
            raise NotFound("Квартира не найдена!")

    def get(self, request, pk, format=None):
        apartment = self.get_object(pk)
        current_user = request.user
        if apartment.owner == current_user:
            serializer = ApartmentSerializer(apartment)
        else:
            serializer = PrettyApartmentSerializer(apartment)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        apartment = self.get_object(pk)
        if apartment.owner == request.user:
            serializer = ChangeApartmentSerializer(apartment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data="У вас нет прав изменять данный объект недвижимости")

    def patch(self, request, pk):
        apartment = self.get_object(pk)
        if apartment.owner == request.user:
            serializer = ChangeApartmentSerializer(apartment, data=request.data,
                                                   partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data="У вас нет прав изменять данный объект недвижимости")

    def delete(self, request, pk, format=None):
        apartment = self.get_object(pk)
        if apartment.owner == request.user:
            apartment.delete()
            return Response(data="Вы успешно удалили объект недвижимости")
        else:
            return Response(data="У вас нет прав удалять данный объект недвижимости")


class ApartmentFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    arrival_date = filters.DateFilter(field_name='orders__departure_date', lookup_expr='gt')
    departure_date = filters.DateFilter(field_name='orders__arrival_date', lookup_expr='lt')
    min_area = filters.NumberFilter(field_name='area__total_area', lookup_expr='gte')
    max_area = filters.NumberFilter(field_name='area__total_area', lookup_expr='lte')
    objects_in_apartment = filters.CharFilter(lookup_expr='icontains')
    nearby_objects = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Apartment
        fields = ['location__region', 'location__city', 'location__district', 'type', 'room', 'floor',
                  'construction_type', 'state',
                  'min_price', 'max_price', 'currency', 'arrival_date', 'departure_date', 'min_area', 'max_area',
                  'objects_in_apartment', 'nearby_objects',
                  'detail__internet', 'detail__furniture', 'detail__heat', 'detail__gas',
                  'detail__phone', 'detail__parking', 'detail__elevator', 'detail__security']


class ApartmentListView(generics.ListAPIView):
    serializer_class = ApartmentsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ApartmentFilter
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        return Apartment.objects.filter(status=True).order_by("-pub_date")


class CreateComment(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Comment.objects.filter(apartment_id=self.kwargs["pk"])
        return queryset

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            try:
                apartments = Apartment.objects.get(id=self.kwargs['pk'])
                return serializer.save(owner=self.request.user, apartment=apartments)
            except ObjectDoesNotExist:
                raise NotFound("Квартира не найдена")
        else:
            raise PermissionDenied('Авторизуйтесь в системе\
             для добавления комментариев')

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
        except ObjectDoesNotExist:
            raise NotFound('Квартира не найдена')

    def get_queryset(self):
        try:
            apartment = Apartment.objects.get(id=self.kwargs['id'])
            if self.request.user == apartment.owner:
                return Booking.objects.filter(apartment__id=self.kwargs['id'])
            else:
                raise PermissionDenied('У вас нету прав на изменение ')
        except ObjectDoesNotExist:
            raise NotFound('Квартира не найдена')


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApartmentImage.objects.all()
    serializer_class = PhotoDetailSerializer


class UploadImage(generics.ListCreateAPIView):
    serializer_class = uploadSerializer
    queryset = Apartment.objects.all()


class NearApartments(generics.ListAPIView):
    serializer_class = ApartmentsSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        pk = self.kwargs['pk']
        from math import radians, cos, sin, asin, sqrt
        try:
            current_apartment = Apartment.objects.get(id=pk)
            dist = 3  # дистанция 3 км радиуса
            mylon = current_apartment.location.longitude
            mylat = current_apartment.location.latitude
            lon1 = mylon - dist / abs(cos(radians(mylat)) * 111.0)
            lon2 = mylon + dist / abs(cos(radians(mylat)) * 111.0)
            lat1 = mylat - (dist / 111.0)
            lat2 = mylat + (dist / 111.0)
            near_apartments = Apartment.objects.filter(location__latitude__range=(lat1, lat2)).filter(
                location__longitude__range=(lon1, lon2)).exclude(id=pk)[:3]
            if not near_apartments:
                raise NotFound("Рядом нет квартир")
            return near_apartments
        except ObjectDoesNotExist:
            raise NotFound('Квартира не найдена')


class PhotoUpdate(APIView):
    def get(self, request, id, pk, format=None):
        try:
            serializer = PhotoDetailSerializer(ApartmentImage.objects.get(id=pk))
        except ObjectDoesNotExist:
            raise NotFound("Квартира не найдена")
        return Response(serializer.data)

    def put(self, request, id, pk, format=None):
        try:
            apartment = Apartment.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise NotFound("Квартира не найдена!")
        if request.user != apartment.owner:
            raise PermissionDenied("Вы не являетесь собственником квартиры")
        try:
            serializer = PhotoDetailSerializer(ApartmentImage.objects.get(id=pk), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except ObjectDoesNotExist:
            raise NotFound("Фотография не найдена")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id, pk):
        try:
            apartment = Apartment.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise NotFound("Квартира не найдена!")
        if request.user != apartment.owner:
            raise PermissionDenied("Вы не являетесь собственником квартиры")
        try:
            serializer = PhotoDetailSerializer(ApartmentImage.objects.get(id=pk), data=request.data,
                                               partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except ObjectDoesNotExist:
            raise NotFound("Фотография не найдена")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, pk, format=None):
        try:
            apartment = Apartment.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise NotFound("Квартира не найдена!")
        if request.user != apartment.owner:
            raise PermissionDenied("Вы не являетесь собственником квартиры")
        try:
            photo = ApartmentImage.objects.get(id=pk)
            photo.delete()
        except ObjectDoesNotExist:
            raise NotFound("Фотография не найдена!")
        return Response(data="Вы успешно удалили фотографию")
