from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(
        User, verbose_name='User as FK', related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name='First name', max_length=100)
    last_name = models.CharField(verbose_name='Last name', max_length=100)
    email = models.CharField(verbose_name='Email', max_length=100)
    address = models.CharField(verbose_name='Address', max_length=100)
    zipcode = models.CharField(verbose_name='Zip', max_length=100)
    place = models.CharField(verbose_name='Place', max_length=100)
    phone = models.CharField(verbose_name='Contact no', max_length=100)
    created_at = models.DateTimeField(verbose_name='Creation date', auto_now_add=True)
    paid_amount = models.DecimalField(verbose_name='Paid amount', 
        max_digits=8, decimal_places=2, blank=True, null=True)
    stripe_token = models.CharField(verbose_name='Token', max_length=100)

    class Meta:
        ordering = ['-created_at', ]
        verbose_name_plural = 'Order' # show on admin page

    def __str__(self):
        return self.first_name
    


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, verbose_name='Order as foreign key',  related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, verbose_name='Product as foreign key', related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='Price', max_digits=8, decimal_places=2)
    quantity = models.IntegerField(verbose_name='Quantity', default=1)

    class Meta:
        verbose_name_plural = 'Order item' # show on admin page

    def __str__(self):
        return '%s' % self.id