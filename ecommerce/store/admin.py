from django.contrib import admin
from .models import ProductModel, OrderModel

# Register your models here.
admin.site.register(ProductModel)
admin.site.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "last_name")
