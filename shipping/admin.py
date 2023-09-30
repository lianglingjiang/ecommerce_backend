from django.contrib import admin
from shipping.models import Country, State, ShippingContact, DeliveryCompany, TrackingInfo


admin.site.register(Country)
admin.site.register(State)
admin.site.register(ShippingContact)
admin.site.register(DeliveryCompany)
admin.site.register(TrackingInfo)
