from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('front-types/', views.TypeView().as_view()),
                  path('front-constructions/', views.ConstructionView().as_view()),
                  path('front-series/', views.SeriesView().as_view()),
                  path('front-states/', views.StateView().as_view()),
                  path('front-countries/', views.CountryView().as_view()),
                  path('front-regions/', views.RegionView().as_view()),
                  path('front-cities/', views.CityView().as_view()),
                  path('front-currency/', views.CurrencyView().as_view()),
                  path('roles/', views.RoleView().as_view()),

                  path('locations/', views.LocationView().as_view()),
                  path('details/', views.DetailView().as_view()),
                  path('contacts/', views.ContactView().as_view()),

                  path('comments/', views.CommentView().as_view()),
                  path('comments/<int:pk>/', views.CommentDetail().as_view()),
                  path('apartment/<int:pk>/comments/', views.CreateComment().as_view()),

                  path('own-apartments/', views.OwnerView().as_view()),
                  path('own-apartments/<int:pk>/upload/', views.UploadImage().as_view()),
                  path('own-apartments/<int:id>/upload/<int:pk>/', views.PhotoDetail().as_view()),
                  path('own-apartments/<int:id>/booking/', views.CreateBooking().as_view()),
                  path('own-apartments/<int:id>/booking/<int:pk>/', views.BookingDetail().as_view()),
                  path('add/', views.ApartmentView().as_view()),
                  path('near/<int:pk>/', views.NearApartments().as_view()),

                  path('apartment/<int:pk>/', views.ApartmentDetail().as_view()),
                  path('apartments/', views.ApartmentListView().as_view()),
                  path('photo/<int:pk>/', views.PhotoUpdate().as_view()),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
