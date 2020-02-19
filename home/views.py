
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from .permissions import IsOwner
from .serializers import *



class TypeView(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = (permissions.IsAdminUser,)


class ImageView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AnnouncementView(generics.ListAPIView):
    serializer_class = AnnouncementSerializer
    queryset = Apartment.objects.all()
    permission_classes = (permissions.AllowAny,)


class ApartmentView(generics.CreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = (permissions.AllowAny,)

#     def perform_create(self, serializers):
#         serializers.save(owner=self.request.user)


class ApartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
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
    
    
class AddressView(generics.CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)



