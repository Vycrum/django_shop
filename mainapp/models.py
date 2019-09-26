from django.db import models
from django.urls import reverse


class ProductCategory(models.Model):
    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

    name = models.CharField(verbose_name="category name", max_length=100)
    description = models.CharField(verbose_name='category description', max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('superadmin:category_detail', args=[str(self.id)])


class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    name = models.CharField(verbose_name='Product name', max_length=128)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    small_image = models.ImageField(verbose_name='Catalog image', upload_to='products_images', blank=True)
    full_image = models.ImageField(verbose_name='Detail image', upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='Short description', max_length=100, blank=True)
    full_desc = models.TextField(verbose_name='Full description', blank=True)
    price = models.DecimalField(verbose_name='Price', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='Stock quantity', default=0)

    def __str__(self):
        return f'{self.name} ({self.category.name})'

    def get_absolute_url(self):
        return reverse('superadmin:product_detail', args=[str(self.id)])