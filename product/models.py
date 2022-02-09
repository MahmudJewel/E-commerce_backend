from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Category for product', max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Category desc' # show on admin page

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Product(models.Model):
    category = models.ForeignKey(
        Category, verbose_name='category as foreign key', related_name='products', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Product name', max_length=255)
    slug = models.SlugField()
    description = models.TextField(verbose_name='Descriptions', blank=True, null=True)
    price = models.DecimalField(verbose_name='Price for each', max_digits=6, decimal_places=2)
    image = models.ImageField(verbose_name='Images', upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(verbose_name='Thumbnail', upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(verbose_name='Added date', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product' # show on admin page
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail