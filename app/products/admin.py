from django.contrib import admin

from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    model = Product
    search_fields = ('name',)
    list_display = [
        'id', 
        'title', 
        'description', 
        'price',
        'quantity', 
        'image_url', 
        'is_active', 
        'created_at', 
        'updated_at',
        ]


admin.site.register(Product, ProductAdmin)