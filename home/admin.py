from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Group

from .models import *

admin.site.register(Type)
admin.site.register(Series)
admin.site.register(Construction)
admin.site.register(State)

admin.site.register(Country)
admin.site.register(Region)

admin.site.site_header = "YourtHome Admin"
admin.site.site_title = "YourtHome Admin"
admin.site.index_title = "Welcome to YourtHome"

admin.site.unregister(Group)


class CommentInline(admin.TabularInline):
    model = Comment
    readonly_fields = ('name_of_publication', 'text_of_publication', 'date_of_publication', 'owner')
    max_num = 0


class BookingInline(admin.TabularInline):
    model = Booking
    readonly_fields = ('arrival_date', 'departure_date')
    max_num = 0


class ImageInline(admin.TabularInline):
    model = ApartmentImage
    readonly_fields = ('image',)
    max_num = 0


class ApartmentAdmin(ModelAdmin):
    fieldsets = (
        ('Об объекте', {'fields': ['title', 'type', 'room', 'floor', 'area', 'location', 'price', 'another_price',
                                   'preview_image', 'pub_date', 'status']}),
        ('Характеристика', {'fields': ['series', 'construction_type', 'state', 'detail', 'nearby_objects',
                                       'objects_in_apartment', 'tags', 'description']}),
        ('Контактная информация', {'fields': ['owner', 'contact']}),
    )

    # readonly_fields = ('title', 'room', 'type', 'floor', 'area', 'detail', 'location', 'owner', 'price', 'description',
    #                    'pub_date', 'another_price')
    readonly_fields = ('pub_date',)
    list_display = ('title', 'type', 'room', 'location', 'pub_date', 'owner', 'status')
    list_editable = ('status',)
    date_hierarchy = 'pub_date'
    inlines = (BookingInline, ImageInline, CommentInline)
    list_filter = ('location__region', 'location__city', 'type', 'room', 'series', 'construction_type', 'state')
    search_fields = ('^title', '^type__type', '^location__city', '^owner__username')
    radio_fields = {'type': admin.VERTICAL, 'series': admin.HORIZONTAL, 'construction_type': admin.HORIZONTAL,
                    'state': admin.HORIZONTAL}
    list_per_page = 20
    actions_on_top = True
    actions_on_bottom = True
    ordering = ['-pub_date']
    save_on_top = True


admin.site.register(Apartment, ApartmentAdmin)
