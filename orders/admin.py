from django.contrib import admin

from .models import Order, OrderItem
from rentalapp.models import MyUser

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'firstname',
        'lastname',
        'email',
        'country',
        'address',
        'postal_code',
        'city',
        'paid',
        'created',
        'updated',
    ]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

