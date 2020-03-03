from django.urls import path, include
from .views import *
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view(), name='registration'),
    path('users/<int:pk>/', UserRetrieveUpdateAPIView.as_view()),
    path('users/', UserView.as_view(), name='users'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('obtain_token/', obtain_jwt_token),
]

urlpatterns += [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
