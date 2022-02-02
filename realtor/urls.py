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
path('uploadhouses/',views.upload_houses,name="uploadhouses"),
path('dashboard/', views.dashboard, name='dashboard'),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)