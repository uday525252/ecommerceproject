from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    image=models.ImageField()
    slug=models.SlugField(max_length=40)
    title=models.CharField(max_length=60)
    description=models.TextField()
    price=models.IntegerField()
    


    def get_absolute_url(self):
        return reverse('hello',kwargs={'slug':self.slug})


class Customer(models.Model):
    name=models.CharField(max_length=60)
    age=models.IntegerField()
    phoneno=models.IntegerField()
    emailid=models.CharField(max_length=100)
    address=models.TextField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.IntegerField()
    totalprice=models.IntegerField()





















