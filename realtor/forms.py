from os import name
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.db import transaction
from functools import partial


DateInput = partial(
    forms.DateInput, {'class': 'datepicker'})



#register as user
class EmployeeSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(
        max_length=60, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EmployeeUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class EmployeeProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'phone_number']



class HouseForm(forms.ModelForm):

    class Meta:
        model = House
        fields = ['title', 'house_type', 'location',
                  'is_rent', 'is_buy', 'price', 'images',
                  'images1','image2','bedroom','shower',"garage",
                  'hse_features','apt_features','description']

    def __init__(self, *args, **kwargs):
        super(HouseForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['house_type'].required = True
        self.fields['location'].required = True
        self.fields['is_rent'].required = False
        self.fields['is_buy'].required = False
        self.fields['images'].required = True
        self.fields['images1'].required = True
        self.fields['images2'].required = True
        self.fields['price'].required = True
        self.fields['garage'].required = False
        self.fields['bedroom'].required = True
        self.fields['shower'].required = False
        self.fields['description'].required = True
        self.fields['apt_features'].required = True
        self.fields['hse_features'].required = True



class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ['title', 'model', 'number_plate','year','images',
        'images1','images2','car_type','price','location']

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['car_type'].required = True
        self.fields['model'].required = True
        self.fields['number_plate'].required = True
        self.fields['year'].required = True
        self.fields['images'].required = True
        self.fields['images1'].required = True
        self.fields['images2'].required = True
        self.fields['price'].required = True
        self.fields['location'].required = True

class LandForm(forms.ModelForm):

    class Meta:
        model = Land
        fields = ['size', 'price', 'location','description','images',
        'images1','images2']

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        self.fields['size'].required = True
        self.fields['price'].required = True
        self.fields['location'].required = True
        self.fields['description'].required = True
        self.fields['images'].required = True
        self.fields['images1'].required = True
        self.fields['images2'].required = True
        

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.IntegerField(required=True)
    email = forms.EmailField(required=False)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Message, please add any additional information.'}), required=True)

    def __str__(self):
        return self.from_email

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.com'
        self.fields['subject'].widget.attrs['placeholder'] = self.fields['subject'].label or 'Subject'