from django.contrib import admin
from users.models import UserProfile, VerifyCode, UserFavorite


class UserProfileAdmin(admin.ModelAdmin):
    fields = ['first_name', 'middle_name', 'last_name',
              'date_of_birth', 'mobile_phone', 'gender',
              'email', 'image']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(VerifyCode)
admin.site.register(UserFavorite)
