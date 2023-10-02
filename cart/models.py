from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product


User = get_user_model()


class Cart(models.Model):
    """Shopping Cart"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    modified = models.DateTimeField(auto_now=True, verbose_name='Modified at')

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Shopping Cart'


class CartEntry(models.Model):
    """
    Cart Entry
    """
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    modified = models.DateTimeField(auto_now=True, verbose_name='Modified at')

    class Meta:
        verbose_name = 'Cart Entry'
        verbose_name_plural = 'Cart Entries'

    def __str__(self):
        return f'{self.product.name}'