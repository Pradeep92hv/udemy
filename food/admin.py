from django.contrib import admin

# Register your models here.

# to display model in admin panel
from .models import Item


admin.site.register(Item)
