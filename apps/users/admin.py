# from django.contrib import admin
# from .models import UserProfile

# admin.site.register(UserProfile)
# # Register your models here.
# Instead of admin.ModelAdmin
# users/admin.py
# from unfold.admin import ModelAdmin  # ← change here
# from django.contrib import admin
# from .models import UserProfile, Match

# @admin.register(UserProfile)
# class UserProfileAdmin(ModelAdmin):
#     list_display = ["user", "location", "travel_style", "budget_level", "adventure_level"]
#     list_filter = ["travel_style", "pace", "budget_level", "adventure_level"]
#     search_fields = ["user__username", "bio", "location"]
#     # add fieldsets, inlines, etc. as usual

# @admin.register(Match)
# class MatchAdmin(ModelAdmin):
#     list_display = ["user1", "user2", "similarity_score", "status", "created_at"]
#     list_filter = ["status"]
#     search_fields = ["user1__username", "user2__username"]
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.contrib.auth.models import Group
from .models import UserLoginHistory


@admin.register(UserLoginHistory)
class UserLoginHistoryAdmin(admin.ModelAdmin):
    list_display = ("user", "login_time", "ip_address")  # Columns shown in admin
    list_filter = ("login_time", "user")                 # Filters for easier tracking
    search_fields = ("user__username", "ip_address")    
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'staff_status', 'superuser_status', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    list_per_page = 20
    fieldsets = (
        ('User Info', {'fields': ('username', 'email', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    def staff_status(self, obj):
        color = "green" if obj.is_staff else "red"
        return format_html('<b style="color:{}">{}</b>', color, obj.is_staff)
    staff_status.short_description = 'Staff'

    def superuser_status(self, obj):
        color = "green" if obj.is_superuser else "red"
        return format_html('<b style="color:{}">{}</b>', color, obj.is_superuser)
    superuser_status.short_description = 'Superuser'

# Unregister the default User admin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)