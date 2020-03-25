from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('types/', views.TypeView().as_view()),
    path('rooms/', views.RoomView().as_view()),
    path('floors/', views.FloorView().as_view()),
    path('constructions/', views.ConstructionView().as_view()),
    path('series/', views.SeriesView().as_view()),
    path('states/', views.StateView().as_view()),
    path('areas/', views.AreaView().as_view()),
    path('countries/', views.CountryView().as_view()),
    path('regions/', views.RegionView().as_view()),
    path('cities/', views.CityView().as_view()),
    path('districts/', views.DistrictView().as_view()),
    path('locations/', views.LocationView().as_view()),
    path('details/', views.DetailView().as_view()),
    path('currency/', views.CurrencyView().as_view()),
    path('roles/', views.RoleView().as_view()),
    path('rents/', views.RentView().as_view()),
    path('contacts/', views.ContactView().as_view()),
    path('comments/', views.CommentView().as_view()),
    path('apartment/<int:pk>/comments/',views.CreateComment().as_view()),
    path('orders/', views.BookingView().as_view()),
    path('own-apartments/', views.OwnerView().as_view()),
    path('own-apartment/<int:pk>/', views.OwnerBookingDetail().as_view()),
    path('images/', views.ImageView().as_view()),
    path('add/', views.ApartmentView().as_view()),
    path('apartment/<int:pk>/', views.ApartmentDetail().as_view()),
    path('apartments/', views.ApartmentListView().as_view()),
    path('ap-type/<int:pk>/', views.ApartmentsTypeView.as_view()),
    path('regions/<int:pk>/', views.RegionsView().as_view()),
    path('cities/<int:pk>/', views.CitiesView().as_view()),
    path('districts/<int:pk>/', views.DistrictsView().as_view()),
    path('ap-region/<int:pk>/', views.ApartmentsRegionView().as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
