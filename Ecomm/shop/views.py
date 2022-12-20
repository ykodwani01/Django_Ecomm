from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
def index(request):
    products=Product.objects.all()
    n=len(products)
    print(products)
    nslides=n//4 + ceil((n/4) + n//4) 
    params={'num_slides':nslides , 'range':range(1,nslides), 'product':products}
    
    return render(request,"index.html",params)
def index2(request):
    return HttpResponse("Index shop tp")

def checkout(request):
    return render(request,"index.html")
def cart(request):
    return render(request,"index.html")
def add(request):
    return render(request,"index.html")
def profile(request):
    return render(request,"about.html")
