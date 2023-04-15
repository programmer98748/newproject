from django.shortcuts import render, redirect
from .models import Products, Category
from django.contrib import messages
# Create your views here.

def index(request):
    #context = {}
    return render(request, 'store/inc/slider.html')

def collections(request):
    category = Category.objects.filter(status=0)

    context = {'category':category}
    return render(request, 'store/collections.html', context)
    
def collectionsviews(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Products.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {
            'products': products,
            'category': category}
        return render(request, 'store/products/index.html', context)
    else:
        messages.warring(request, f"no sush category found")
        return redirect('collections')

def productview(request, cate_slug, prod_slug):
    if (Category.objects.filter(slug=cate_slug, status=0)):
        if(Products.objects.filter(slug=prod_slug, status=0)):
            products = Products.objects.filter(slug=prod_slug, status=0).first()     
            context = {'products': products}
        else:
            messages.error(request, "no sush category found")
            return redirect('collections')           
    else:
        messages.error(request, "no sush category found")       
        return redirect('collections')
    return render(request, 'store/products/view.html', context)