from django.shortcuts import render, redirect
#from .models import Products, Category
from django.contrib import messages
# Create your views here.

def index(request):
    #context = {}
    return render(request, 'store/inc/slider.html')

