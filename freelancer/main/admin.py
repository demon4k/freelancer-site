from django.contrib import admin
from .models import Category, Product, Order, OrderItem

admin.site.register(Category)
admin.site.register(Product)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_email', 'created_at')
    search_fields = ('customer_name', 'customer_email', 'address')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
