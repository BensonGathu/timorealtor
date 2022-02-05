from multiprocessing import context
from unicodedata import name
from django.forms import forms
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants as messages
from django.contrib import messages

# Create your views here.

def employee_registration(request):
    if request.method == 'POST':
        form = EmployeeSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('username')
            messages.success(
                request, first_name + ' ' + 'your account was created successfully!')
            return redirect('login')
    else:
        form = EmployeeSignUpForm()

    context = {
        'form': form
    }
    return render(request, 'auth/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,
                            password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in as' + ' ' + username)

            return redirect('home')
        else:
            messages.error(request, 'Invalid Username or Password')

    context = {}
    return render(request, 'auth/login.html', context)


def logoutUser(request):
    logout(request)
    messages.info(
        request, 'You have logged out. Log back in to update schedule.')
    return redirect('home')


@login_required
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        u_form = EmployeeUpdateForm(request.POST, instance=request.user)
        p_form = EmployeeProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.employee)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = EmployeeUpdateForm(instance=request.user)
        p_form = EmployeeProfileUpdateForm(instance=request.user.employee)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'current_user': current_user,
    }
    return render(request, 'profile.html', context)


@login_required
def dashboard(request):
    house_count = House.objects.count()
    land_count = Land.objects.count()
    car_count = Car.objects.count()

    context = {"house_count":house_count,
                "land_count":land_count,
                "car_count":car_count
                 }
    return render(request, 'dashboard/dashboard.html', context)


def home(request):
    current_user = request.user
    all_cars = Car.objects.all().order_by('-id')[:3] 
    all_land = Land.objects.all().order_by('-id')[:3] 
    all_houses = House.objects.all().order_by('-id')[:3] 
    context = {"current_user":current_user,
                "all_cars":all_cars,
                "all_land":all_land,
                "all_houses":all_houses
                }
    all_data = []
    return render(request,"home.html",context)

#view to upload Houses
def upload_houses(request):
    current_user = request.user
    form = HouseForm(request.POST or None,
                           request.FILES or None)
    if current_user.is_authenticated:
        if request.method == 'POST':
            form = HouseForm(
                request.POST or None, request.FILES or None)
            if form.is_valid():
                form.employee = current_user
                form.save()
                messages.success(
                    request, f'You have successfully uploaded a house.')
                return redirect('dashboard')

    context = {'form': form,
               'current_user': current_user
               }
    return render(request, 'dashboard/uploadhouses.html', context)


#view to upload cars
def upload_cars(request):
    current_user = request.user
    form = CarForm(request.POST or None,
                           request.FILES or None)
    if current_user.is_authenticated:
        if request.method == 'POST':
            form = CarForm(
                request.POST or None, request.FILES or None)
            if form.is_valid():
                form.employee = current_user
                form.save()
                messages.success(
                    request, f'You have successfully uploaded a car.')
                return redirect('dashboard')

    context = {'form': form,
               'current_user': current_user
               }
    return render(request, 'dashboard/uploadcar.html', context)


#view to upload land
def upload_land(request):
    current_user = request.user
    form = LandForm(request.POST or None,request.FILES or None)
    if current_user.is_authenticated:
        if request.method == 'POST':
            form = LandForm(
                request.POST or None, request.FILES or None)
            if form.is_valid():
                form.employee = current_user
                form.save()
                messages.success(
                    request, f'Land successfully uploaded.')
                return redirect('dashboard')

    context = {'form': form,
               'current_user': current_user
               }
    return render(request, 'dashboard/uploadland.html', context)

def car_details(request,id):
    selected_property = get_object_or_404(Car,pk=id)
    context = {"selected_property":selected_property}
    return render(request, 'cardetails.html', context)




