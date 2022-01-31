from unicodedata import name
from django.shortcuts import render

# Create your views here.
def home(request):
    name="Timo"
    context = {"name":name}
    return render(request,"home.html",context)
