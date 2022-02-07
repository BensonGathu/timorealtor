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
path('car_details/<int:id>',views.car_details,name="car_details"),
path('house_details/<int:id>',views.house_details,name="house_details"),
path('land_details/<int:id>',views.land_details,name="land_details"),
path('buyland',views.buyland,name="buyland"),
path('rentland',views.rentland,name="rentland"),
path('buycar',views.buycar,name="buycar"),
path('rentcar',views.rentcar,name="rentcar"),
path('buyhouse',views.buyhouse,name="buyhouse"),
path('renthouse',views.renthouse,name="renthouse"),



]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)