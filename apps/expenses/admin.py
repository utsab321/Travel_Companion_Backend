from django.contrib import admin
from .models import Expense
# Register your models hfrom .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("trip", "amount", "paid_by", "date")
    search_fields = ("trip__title", "paid_by__username")
    list_filter = ("date",)
    ordering = ("-date",)
