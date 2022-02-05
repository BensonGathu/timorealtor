from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
path("",views.home,name="home"),
path('register/', views.employee_registration,name='registration'),
path('login/', views.loginPage, name='login'),
path('logout/', views.logoutUser, name='logout'),
path('profile/', views.profile, name='profile'),
path('dashboard/', views.dashboard, name='dashboard'),
path('addhouses/',views.upload_houses,name="addhouses"),
path('addcars/',views.upload_cars,name="addcars"),
path('addland/',views.upload_land,name="addland"),
path('car_details/<int:id>',views.car_details,name="details"),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)