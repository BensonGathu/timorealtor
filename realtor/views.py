from multiprocessing import context
from unicodedata import name
from django.forms import forms
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.core.mail import send_mail, BadHeaderError

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


@login_required(login_url='login')
def dashboard(request):
    house_count = House.objects.count()
    land_count = Land.objects.count()
    car_count = Car.objects.count()
    total_count = house_count+ land_count+car_count

    context = {"house_count":house_count,
                "land_count":land_count,
                "car_count":car_count,
                "total_count":total_count
                 }
    return render(request, 'dash/dashboard.html', context)


def home(request):
    if request.method == "POST":
        message_name = request.POST.get("name")
        message_phone = request.POST.get("phone")
        message_email = request.POST.get("email")
        message_subject = request.POST.get("subject")
        message = request.POST["message"]

        data = {"message_name":message_name,
                "message_phone":message_phone,
                "message_email":message_email,
                "message_subject":message_subject,
                "message":message
                    }
        message = '''New message:{}  
                From:{}   
                Phone Number:{}
                '''.format(data['message'], data['message_email'],data['message_phone'])
        send_mail(data['message_subject'],message,data['message_email'],['Morric150@gmail.com'])
        messages.success(
                    request, f"ThankYou for Emailing Us. We'll get back to you Shortly.")

    current_user = request.user
    all_cars = Car.objects.all().order_by('-id')[:3] 
    all_land = Land.objects.all().order_by('-id')[:3] 
    all_houses = House.objects.all().order_by('-id')[:3] 
    c_images = []
    for car in all_cars:
        c_images.append(car.images.url)

    for land in all_land:
        c_images.append(land.images.url)
    
    for house in all_houses:
        c_images.append(house.images.url)

    print(c_images)
    context = {"current_user":current_user,
                "all_cars":all_cars,
                "all_land":all_land,
                "all_houses":all_houses,
                "c_images":c_images
                
                }
    all_data = []
        
   
    return render(request,"home.html",context)
    

#view to upload Houses
@login_required
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
    return render(request, 'dash/uploadhouses.html', context)


#view to upload cars
@login_required
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
    return render(request, 'dash/uploadcar.html', context)


#view to upload land
@login_required
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
    return render(request, 'dash/uploadland.html', context)

#single item
def car_details(request,id):
    if request.method == "POST":
        message_name = request.POST.get("name")
        message_phone = request.POST.get("phone")
        message_email = request.POST.get("email")
        message_subject = request.POST.get("subject")
        message = request.POST["message"]

        data = {"message_name":message_name,
                "message_phone":message_phone,
                "message_email":message_email,
                "message_subject":message_subject,
                "message":message
                    }
        message = '''New message:{}  
                From:{}   
                Phone Number:{}
                '''.format(data['message'], data['message_email'],data['message_phone'])
        send_mail(data['message_subject'],message,data['message_email'],['Morric150@gmail.com'])
        messages.success(
                    request, f"ThankYou for showing interest in our product. We'll get back to you Shortly.")
    selected_property = get_object_or_404(Car,pk=id)
    context = {"selected_property":selected_property}
    return render(request, 'singlecardetails.html', context)

def house_details(request,id):
    if request.method == "POST":
        message_name = request.POST.get("name")
        message_phone = request.POST.get("phone")
        message_email = request.POST.get("email")
        message_subject = request.POST.get("subject")
        message = request.POST["message"]

        data = {"message_name":message_name,
                "message_phone":message_phone,
                "message_email":message_email,
                "message_subject":message_subject,
                "message":message
                    }
        message = '''New message:{}  
                From:{}   
                Phone Number:{}
                '''.format(data['message'], data['message_email'],data['message_phone'])
        send_mail(data['message_subject'],message,data['message_email'],['Morric150@gmail.com'])
        messages.success(
                    request, f"ThankYou for showing interest in our product. We'll get back to you Shortly.")
    selected_property = get_object_or_404(House,pk=id)
    context = {"selected_property":selected_property}
    return render(request, 'singlehousedetails.html', context)

def land_details(request,id):
    if request.method == "POST":
        message_name = request.POST.get("name")
        message_phone = request.POST.get("phone")
        message_email = request.POST.get("email")
        message_subject = request.POST.get("subject")
        message = request.POST["message"]

        data = {"message_name":message_name,
                "message_phone":message_phone,
                "message_email":message_email,
                "message_subject":message_subject,
                "message":message
                    }
        message = '''New message:{}  
                From: {}   
                Phone Number:{}
                '''.format(data['message'], data['message_email'],data['message_phone'])
        send_mail(data['message_subject'],message,data['message_email'],['Morric150@gmail.com'])
        messages.success(
                    request, f"ThankYou for showing interest in our product. We'll get back to you Shortly.")
    selected_property = get_object_or_404(Land,pk=id)
    context = {"selected_property":selected_property}
    return render(request, 'singlelanddetails.html', context)


 #filter option for specific properties
def buyland(request):
    selected_property = Land.objects.filter(is_buy=True)
    context = {
        "buy":"buy",
        "selected_property":selected_property,
    }
    return render(request, 'lands.html', context)
def rentland(request):
    selected_property = Land.objects.filter(is_rent=True)
    context = {
        "rent":"rent",
        "selected_property":selected_property,
    }
    return render(request, 'lands.html', context)


def buycar(request):
    selected_property = Car.objects.filter(is_buy=True)
    context = {
        "buy":"buy",
        "selected_property":selected_property,
    }
    return render(request, 'cars.html', context)
def rentcar(request):
    selected_property = Car.objects.filter(is_rent=True)
    context = {
        "rent":"rent",
        "selected_property":selected_property,
    }
    return render(request, 'cars.html', context)


def buyhouse(request):
    selected_property = House.objects.filter(is_buy=True)
    context = {
        "buy":"buy",
        "selected_property":selected_property,
    }
    return render(request, 'houses.html', context)
   
def renthouse(request):
    selected_property = House.objects.filter(is_rent=True)
    context = {
        "rent":"rent",
        "selected_property":selected_property,
    }
    return render(request, 'houses.html', context)

#update properties
@login_required(login_url='login')
def updatecar(request,id):
    current_property = get_object_or_404(Car,pk=id)
    
    if request.method == 'POST':
        form = CarUpdateForm(
                request.POST,request.FILES, instance=current_property)
        if form.is_valid():
            form.save()
            messages.success(request, f'Property successfully updated!')
        return redirect('mycars')
    else:
        form = CarUpdateForm(instance=current_property)
    context = {'form': form,
                'current_propert': current_property,
                }
    
    return render(request, 'dash/uploadcar.html', context)


@login_required(login_url='login')
def updatehouse(request,id):
    current_property = get_object_or_404(House,pk=id)
   
    if request.method == 'POST':
        form = HouseUpdateForm(
                request.POST,request.FILES, instance=current_property)
        if form.is_valid():
            form.save()
            messages.success(request, f'Property successfully updated!')
        return redirect('myhouses')
    else:
        form = HouseUpdateForm(instance=current_property)
    context = {'form': form,
                'current_propert': current_property,
                }
    
    return render(request, 'dash/uploadhouses.html', context)


@login_required(login_url='login')
def updateland(request,id):
    current_property = get_object_or_404(Land,pk=id)
   
    if request.method == 'POST':
        form = LandUpdateForm(
                request.POST,request.FILES, instance=current_property)
        if form.is_valid():
            form.save()
            messages.success(request, f'Property successfully updated!')
        return redirect('mylands')
    else:
        form = LandUpdateForm(instance=current_property)
    context = {'form': form,
                'current_propert': current_property,
                }
    
    return render(request, 'dash/uploadland.html', context)

@login_required(login_url='login')
def mylands(request):
    selected_property = Land.objects.all()
    context = {
        
        "selected_property":selected_property,
    }
    return render(request, 'dash/mylands.html', context)

@login_required(login_url='login')
def myhouses(request):
    selected_property = House.objects.all()
    context = {
        
        "selected_property":selected_property,
    }
    return render(request, 'dash/myhouses.html', context)

@login_required(login_url='login')
def mycars(request):
    selected_property = Car.objects.all()
    context = {
        
        "selected_property":selected_property,
    }
    return render(request, 'dash/mycars.html', context)

@login_required(login_url='login')
def delete_car(request, id):
    job = get_object_or_404(Car, pk=id)
    if job:
        job.delete()
        messages.success(
            request, f'Car successfully deleted.')
        return redirect('mycars')

@login_required(login_url='login')
def delete_house(request, id):
    job = get_object_or_404(House, pk=id)
    if job:
        job.delete()
        messages.success(
            request, f'Land successfully deleted.')
        return redirect('myhouses')

@login_required
def delete_land(request, id):
    job = get_object_or_404(Land, pk=id)
    if job:
        job.delete()
        messages.success(
            request, f'Land successfully deleted.')
        return redirect('mylands')


# def contactView(request):
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             phone = form.cleaned_data['phone']
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject, message, from_email, ['admin@example.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('success')
#     return render(request, "home.html", {'form': form})

