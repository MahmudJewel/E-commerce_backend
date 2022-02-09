from django.contrib import admin
from order.models import Order, OrderItem
# Register your models here.

lst = [Order, OrderItem]
admin.site.register(lst)