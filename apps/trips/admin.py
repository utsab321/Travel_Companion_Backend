from django.contrib import admin
from .models import Trip
from .models import City, ItineraryItem,Destination

admin.site.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')
    search_fields = ('name',)
admin.site.register(ItineraryItem)
class ItineraryItemAdmin(admin.ModelAdmin):
    list_display = ("trip", "name", "date", "description")
    search_fields = ("name", "trip__title")

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'location')
    list_filter = ('city',)
    search_fields = ('name', 'city__name')

@admin.register(Trip)

class TripAdmin(admin.ModelAdmin):
    list_display = ("title", "creator", "destination", "start_date", "end_date")
    search_fields = ("title", "creator__username")
    list_filter = ("destination", "start_date")
    ordering = ("-start_date",)
# Register your models here.
