from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Type)
admin.site.register(Image)
admin.site.register(Apartment)
admin.site.register(Address)



