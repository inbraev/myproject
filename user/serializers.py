from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'phone', 'name', 'surname')
        extra_kwargs = {'password': {'write_only': True}}


class RegistrationSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            name=validated_data['name'],
            surname=validated_data['surname'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'phone', 'name', 'surname']
        
