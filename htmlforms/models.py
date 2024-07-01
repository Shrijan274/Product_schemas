from django.db import models
from django.utils import timezone

class User(models.Model):
    email = models.EmailField(max_length=64)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    password = models.CharField(max_length=128) 

    
    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.email}) - Password: {self.password}"
    
    
class Product(models.Model):
    productName= models.CharField(max_length=32)
    schema= models.JSONField(default=dict)
    is_active = models.BooleanField(default=True,null=True,blank=True)
    inserted_time=models.DateTimeField(default=timezone.now)
    updated_time= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.productName

class Item(models.Model):
    item=models.CharField(max_length=32)
    brand=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8, decimal_places=2)
    description=models.TextField()
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    formschema=models.JSONField(default=dict)
    is_available=models.BooleanField(default=True,null=True,blank=True)

    def __str__(self):
        return f"Brand:{self.brand} Item name:{self.item}"

