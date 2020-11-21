from django.contrib import admin

from .models import Customer
from .models import Address

admin.site.register(Customer)
admin.site.register(Address)