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
    inserted_time= models.DateTimeField(auto_now_add=True)
    updated_time= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.productName
