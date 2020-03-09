from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from .permissions import IsOwner
from .serializers import *


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
    permission_classes = (permissions.IsAdminUser,)


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


class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (permissions.AllowAny,)


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


class ApartmentListView(generics.ListAPIView):
    serializer_class = ApartmentsSerializer
    queryset = Apartment.objects.all()
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
