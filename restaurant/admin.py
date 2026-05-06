from django.contrib import admin

from .models import Booking, Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'no_of_guests', 'bookingdate')
    list_filter = ('bookingdate',)
    search_fields = ('name',)
