from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('types/', views.TypeView().as_view()),
    path('images/', views.ImageView().as_view()),
    path('address/', views.AddressView().as_view()),
    path('apartment/', views.ApartmentView().as_view()),
    path('apartment/<int:pk>/', views.ApartmentDetail().as_view()),
    path('announcements/', views.AnnouncementView().as_view()),
    path('apartment-type/<int:pk>/', views.ApartmentsTypeView.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
