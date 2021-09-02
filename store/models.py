from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, TextField

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    discounted_Price =models.FloatField()
    category = models.CharField(max_length=300)
    discription = models.TextField()
    image = models.CharField(max_length=500)

    # __str__(self):
    #     return self.title

class Order(models.Model):
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    address= models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=150) 
    zipcode = models.CharField(max_length=200)
    items = models.CharField(max_length=1500)
    totalPrice= models.CharField(max_length=300)

  