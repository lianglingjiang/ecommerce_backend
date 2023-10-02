from django.contrib import admin
from products.models import Category, Brand, Product, ProductImage, HeroImage


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'category', 'sku', 'price', 'in_stock']
    inlines = [
        ProductImageAdmin,
    ]


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(HeroImage)
