from django.contrib import admin
from products.models import Category, Brand, Product, ProductImage, HeroImage


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(HeroImage)
