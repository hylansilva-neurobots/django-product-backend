from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=500)
    price = models.FloatField(blank=False, default=0.00)
    quantity = models.IntegerField(blank=False)
    image_url = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(default=None)