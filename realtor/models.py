from pyexpat import model
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import datetime, timedelta

# Create your models here.

class Employee(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=60, blank=True, null=True)
    phone_number = models.CharField(max_length=70, blank=True)

    # profile_pic = models.ImageField(upload_to='employee_pics/',
    #                                 blank=True)
    

    def __str__(self):
        return self.user

    def save_employee(self):
        self.save()

    def update_employee(self, using=None, fields=None, **kwargs):
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()
            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
        super().refresh_from_db(using, fields, **kwargs)

    def delete_employee(self):
        self.delete()

    def create_employee_profile(sender, **kwargs):
        if kwargs['created']:
            employee_profile = Employee.objects.create(
                user=kwargs['instance'])

    post_save.connect(create_employee_profile, sender=User)



house_types = (
    ("Bungalow","Bungalow"),
    ("Massionete","Massionete"),
    ("Penthouse","Penthouse"),
)

class House(models.Model):
    employee = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    title = models.CharField(max_length=200,blank=True,null=True)
    house_type = models.CharField(choices=house_types,max_length=2000)
    location = models.CharField(max_length=200,blank=True,null=True)
    is_rent = models.BooleanField(default=False)
    is_buy = models.BooleanField(default=False)
    price =  models.CharField(max_length=200,blank=True,null=True)
    images = models.ImageField(upload_to='images/')
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    bedroom = models.IntegerField()
    shower = models.IntegerField()
    garage = models.IntegerField()
    hse_features = models.TextField(max_length=2500, blank=True)
    apt_features = models.TextField(max_length=2500, blank=True)
    description = models.TextField(max_length=2500, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

     
    def __str__(self):
        return self.title
 
car_types = (
    ("Vehicle Parts & Accessories","Vehicle Parts & Accessories"),
    ("Car","Car"),
    ("Trucks & Trailers","Trucks & Trailers"),
    ("Buses & Microbuses","Buses & Microbuses"),
    ("Heavy Equipments","Heavy Equipments"),
    ("Watercrafts & Boats","Watercrafts & Boats"),
)
transmission_type = (
    ("Manual","Manual"),
    ("Automatic","Automatic"),
)

fuel_type = (
    ("Petrol","Petrol"),
    ("Diesel","Diesel"),
)

class Car(models.Model):
    employee = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    car_type = models.CharField(choices=car_types,max_length=2000,blank=True,null=True)
    description = models.TextField(max_length=2000,blank=True,null=True)
    title = models.CharField(max_length=200,blank=True,null=True)
    model = models.CharField(max_length=200,blank=True,null=True)
    number_plate = models.CharField(max_length=200,blank=True,null=True)
    year = models.IntegerField()
    transmission = models.CharField(choices=transmission_type,max_length=2000,blank=True,null=True)
    fuel = models.CharField(choices=fuel_type,max_length=2000,blank=True,null=True)
    seats = models.IntegerField()
    is_rent = models.BooleanField(default=False)
    is_buy = models.BooleanField(default=False)
    images = models.ImageField(upload_to='images/')
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    price =  models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Land(models.Model):
    employee = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    title = models.CharField(max_length=200,blank=True,null=True)
    size = models.CharField(max_length=200,blank=True,null=True)
    price =  models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    is_rent = models.BooleanField(default=False)
    is_buy = models.BooleanField(default=False)
    description =  models.TextField(max_length=200,blank=True,null=True)
    images = models.ImageField(upload_to='images/')
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.description


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
 
    def __str__(self):
        return self.message
 
    class Meta:
        ordering = ('timestamp',)
 
    

