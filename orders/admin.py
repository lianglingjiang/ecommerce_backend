from django.contrib import admin
from orders.models import Order, OrderItem


class OrderItemAdmin(admin.StackedInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'order_num', 'tracking_info', 'payment_status', 'payment_time', 'order_status']
    inlines = [
        OrderItemAdmin,
    ]


admin.site.register(Order, OrderAdmin)