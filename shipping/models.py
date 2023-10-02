from django.db import models
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField

User = get_user_model()


class Country(models.Model):
    code = CountryField()
    name = models.CharField(max_length=127)

    class Meta:
        verbose_name_plural = 'countries'

    def __unicode__(self):
        return u"%s (%s)" % (self.name, self.code)

    def __str__(self):
        return f'{self.name}'


class State(models.Model):
    short_name = models.CharField(max_length=127)
    long_name = models.CharField(max_length=254)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('short_name', 'country')

    def __unicode__(self):
        return u"%s, %s" % (self.long_name, self.country.code)

    def __str__(self):
        return f'{self.long_name}'


class ShippingContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    primary = models.BooleanField(default=False)

    first_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='First Name')
    middle_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Middle Name')
    last_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Last Name')

    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255, null=True, blank=True)
    line3 = models.CharField(max_length=255, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=31, blank=True)

    number = models.CharField(max_length=63, db_index=True)
    type = models.PositiveSmallIntegerField(choices=[(1, 'Fixed'), (2, 'Cell'), (3, 'Fax')])

    email = models.EmailField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    modified = models.DateTimeField(auto_now=True, verbose_name='Modified at')

    def __unicode__(self):
        rv = self.line1
        if self.line2:
            rv += ', ' + self.line2
        if self.line3:
            rv += ', ' + self.line3
        rv += ', ' + self.city
        rv += ', ' + self.state.short_name
        if self.zip:
           rv += ', ' + self.zip
        rv += ', ' + str(self.state.country.code)
        return rv

    def __str__(self):
        return self.__unicode__()

    def url(self):
        return 'mailto:%s' % self.email

    class Meta:
        verbose_name = 'Shipping Contact'
        verbose_name_plural = 'Shipping Contacts'


class DeliveryCompany(models.Model):
    company_name = models.CharField(max_length=20, unique=True, verbose_name='Delivery Company Name')
    email = models.EmailField()
    number = models.CharField(max_length=63, db_index=True)
    type = models.PositiveSmallIntegerField(choices=[(1, 'Fixed'), (2, 'Cell'), (3, 'Fax')])

    def __unicode__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Delivery Company'
        verbose_name_plural = 'Delivery Companies'

    def __str__(self):
        return self.company_name


class TrackingInfo(models.Model):
    tracking_num = models.CharField(max_length=30, unique=True, verbose_name='Tracking Number')
    delivery_company = models.ForeignKey(DeliveryCompany, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Tracking Info'
        verbose_name_plural = 'Tracking Infos'

    def __str__(self):
        return f'{self.delivery_company} {self.tracking_num}'
