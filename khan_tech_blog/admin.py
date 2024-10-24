from django.contrib import admin
from .models import ToDOList, Item
# Register your models here.
admin.site.register(ToDOList)
admin.site.register(Item)