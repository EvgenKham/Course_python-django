from django.contrib import admin
from orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product', ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'phone_number', 'created', ]
    list_filter = ['created', ]
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
