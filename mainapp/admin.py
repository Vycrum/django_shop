from django.contrib import admin
from mainapp.models import ProductCategory, Product


admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'name', 'category', 'price', 'quantity',
    # list_filter = 'quantity',
    search_fields = 'name', 'category'
    readonly_fields = 'quantity',
    sortable_by = 'name', 'category', 'price', 'quantity',
