from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Product


class UserProfile(AbstractUser):
    """User Profile"""
    GENDERS = (
        ('female', 'Female'),
        ('male', 'Male'),
        ('non-binary', 'Non-Binary'),
        ('other', 'Other'),
        ('none', 'Prefer not to Answer')
    )

    first_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='First Name')
    middle_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Middle Name')
    last_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Last Name')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Date of Birth')
    mobile_phone = models.CharField(max_length=20, verbose_name='Mobile Phone', unique=True)
    gender = models.CharField(null=True, blank=True, max_length=20, verbose_name='Gender', choices=GENDERS)
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='Email')
    image = models.ImageField(upload_to='avatar/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    modified = models.DateTimeField(auto_now=True, verbose_name='Modified at')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        if self.middle_name is not None:
            return f'{self.first_name} {self.middle_name} {self.last_name}'
        else:
            return f'{self.first_name} {self.last_name}'


class VerifyCode(models.Model):
    """Verify Code"""
    code = models.CharField()
    mobile_phone = models.CharField(max_length=20, verbose_name='Mobile Phone', unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Sent at')

    class Meta:
        verbose_name = 'Verify Code'
        verbose_name_plural = 'Verify Codes'

    def __str__(self):
        return f'{self.mobile_phone}: {self.code} sent at: {self.created}'


class UserFavorite(models.Model):
    """User Favorite List"""
    user = models.ForeignKey(UserProfile, verbose_name='User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'

    def __str__(self):
        return f'{self.user.first_name} {self.user.middle_name} {self.user.last_name}'
