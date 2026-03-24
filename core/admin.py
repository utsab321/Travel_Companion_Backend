from django.contrib import admin
from .models import Destination

class DestinationAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = ("name", "country",  "description")
    
    # Fields that can be searched in the admin search bar
    search_fields = ("name", "country")
    
    # Filters on the right sidebar
    list_filter = ("country",)
    
    # Default ordering of records
    ordering = ("name",)

# Register the model with the custom admin configuration
admin.site.register(Destination, DestinationAdmin)