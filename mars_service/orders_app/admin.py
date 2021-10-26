from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Order

admin.site.register(Order)
