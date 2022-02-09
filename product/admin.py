from django.contrib import admin
from product.models import Category, Product
# Register your models here.

lst = [Category,Product]
admin.site.register(lst)
