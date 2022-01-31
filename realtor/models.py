from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.
house_types = (
    ("Massionette","Massionette")
)

class House(models.Model):
    title = models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    is_rent = models.BooleanField(default=False)
    is_buy = models.BooleanField(default=False)
    price =  models.FloatField()
    images = models.ImageField(upload_to='images/')
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    bedroom = models.IntegerField()
    shower = models.IntegerField()
    garage = models.IntegerField()
    hse_features = models.IntegerField()
    apt_features = models.IntegerField()
    house_type = models.CharField(choices=house_types,max_length=2000)
    location = models.CharField(max_length=200,blank=True,null=True)

     
    def __str__(self):
        return self.title

class Car(model.Model):
    title = models.CharField(max_length=200,blank=True,null=True)
    model = models.CharField(max_length=200,blank=True,null=True)
    number_plate = models.CharField(max_length=200,blank=True,null=True)
    year = models.IntegerField()
    images = models.ImageField(upload_to='images/')
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    car_type = models.CharField(max_length=200,blank=True,null=True)
    price =  models.FloatField()
    location = models.CharField(max_length=200,blank=True,null=True)


    def __str__(self):
        return self.title

class Land(models.Model):
    size = models.CharField(max_length=200,blank=True,null=True)
    price =  models.FloatField()
    location = models.CharField(max_length=200,blank=True,null=True)
    description =  models.CharField(max_length=200,blank=True,null=True)
    images = models.ImageField(upload_to='images/')
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')


    

