from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    """Product Category"""
    CATEGORY_TYPE = (
        (1, 'Level 1'),
        (2, 'Level 2'),
        (3, 'Level 3'),
    )

    name = models.CharField(default='', max_length=30, verbose_name='Category name')
    code = models.CharField(default='', max_length=30, verbose_name='Category code')
    desc = models.TextField(default='', verbose_name='Category description')
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name='Category type')
    parent_category = models.ForeignKey('self', blank=True, null=True,
                                        related_name='subcategory',
                                        verbose_name='Parent Category',
                                        on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False, verbose_name='Is featured')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    modified = models.DateTimeField(auto_now=True, verbose_name='Modified at')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Brand(models.Model):
    """Product Brand"""
    name = models.CharField(max_length=20, verbose_name='Brand name')
    desc = models.TextField(max_length=255, verbose_name='Brand description')
    image = models.ImageField(upload_to='brands/', verbose_name='Brand logo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    modified = models.DateTimeField(auto_now=True, verbose_name='Modified at')

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product"""
    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.CASCADE,
                                 verbose_name='Product Category')
    sku = models.CharField(max_length=50, default='', verbose_name='SKU', unique=True)
    name = models.CharField(max_length=255, verbose_name='Product Name')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Brand')
    in_stock = models.IntegerField(default=0, verbose_name='In Stock')
    discount = models.BooleanField(default=False, verbose_name='On Sale')
    discount_rate = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Discount Rate (%)')
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Price')
    short_desc = models.TextField(max_length=500, verbose_name='Short Description')
    desc = RichTextField(verbose_name='Description')
    free_shipping = models.BooleanField(default=False, verbose_name='Free Shipping')
    thumbnail = models.ImageField(upload_to='product_images/', null=True, blank=True, verbose_name='Thumbnail')
    is_new = models.BooleanField(default=False, verbose_name='New Arrival')
    is_featured = models.BooleanField(default=False, verbose_name='Featured')
    clicks_count = models.IntegerField(default=0, verbose_name='Total Clicks')
    sold_count = models.IntegerField(default=0, verbose_name='Total Sold')
    favorites_count = models.IntegerField(default=0, verbose_name='Total Favorite')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    modified = models.DateTimeField(auto_now=True, verbose_name='Modified at')

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    """Product Images"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    image = models.ImageField(upload_to='product_images/', null=True, blank=True, verbose_name='Product Images')
    image_url = models.CharField(max_length=300, null=True, blank=True, verbose_name='Image URL')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    modified = models.DateTimeField(auto_now=True, verbose_name='Modified at')

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return self.product.name


class HeroImage(models.Model):
    """Hero Image"""
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hero/', verbose_name='Hero Image')
    index = models.IntegerField(default=0, verbose_name='Index')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    modified = models.DateTimeField(auto_now=True, verbose_name='Modified at')

    class Meta:
        verbose_name = 'Hero Image'
        verbose_name_plural = 'Hero Images'

    def __str__(self):
        return self.product.name