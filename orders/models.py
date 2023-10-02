from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
from shipping.models import ShippingContact, TrackingInfo


User = get_user_model()


class Order(models.Model):

    PAYMENT_STATUS = (
        ('success', 'Success'),
        ('pending', 'Pending'),
        ('canceled', 'Canceled'),
        ('processing', 'Processing'),
        ('error', 'Error')
    )

    ORDER_STATUS = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
        ('awaiting_payment', 'Awaiting Payment'),
        ('partially_shipped', 'Partially Shipped'),
        ('returned', 'Returned'),
        ('refunded', 'Refunded'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_num = models.CharField(max_length=30, unique=True, verbose_name='Order Number')
    tracking_info = models.ForeignKey(TrackingInfo, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Tracking Info')
    payment_id = models.CharField(max_length=100, unique=True, verbose_name='Payment ID')
    payment_status = models.CharField(choices=PAYMENT_STATUS, verbose_name='Payment Status')
    payment_time = models.DateTimeField(null=True, blank=True, verbose_name='Payment Time')

    shipping_contact = models.ForeignKey(ShippingContact, on_delete=models.PROTECT, verbose_name='Shipping Contact')
    order_status = models.CharField(choices=ORDER_STATUS, null=True, blank=True, verbose_name='Order Status')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    modified = models.DateTimeField(auto_now=True, verbose_name='Modified at')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'{self.order_num} {self.created}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.IntegerField(default=0, verbose_name='Quantity')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
