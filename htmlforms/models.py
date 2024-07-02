from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
    productName= models.CharField(max_length=32)
    schema= models.JSONField(default=dict)
    is_active = models.BooleanField(default=True,null=True,blank=True)
    inserted_time=models.DateTimeField(default=timezone.now)
    updated_time= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.productName

class Item(models.Model):
    product=models.ForeignKey(Product, on_delete=models.SET_NULL,null=True,blank=True)
    data=models.JSONField(default=dict)
    is_available=models.BooleanField(default=True,null=True,blank=True)
    user=models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)


