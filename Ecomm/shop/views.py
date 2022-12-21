from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
import js2py
# Create your views here.
def index(request):
    products=Product.objects.all()
    n=len(products)
    print(products)
    nslides=n//4 + ceil((n/4) + n//4) 
    params={'num_slides':nslides , 'range':range(1,nslides), 'product':products}
    
    return render(request,"index.html",params)

def cart(request):
    # return render(request,"index.html")
    # js2py("console.log('hello');")
    # res_2 = js2py.eval_js(localStorage.getItem('cart'))
    # print(res_2)
    return render(request,"checkout.html")
def checkout(request):
    return render(request,"checkout.html")
def add(request):
    return render(request,"index.html")
def profile(request):
    return render(request,"about.html")
def search(request):
    return render(request,"about.html")

def detail(request,myid):
    #fetching the product using id
    product=Product.objects.filter(id=myid)
    print(product)
    params={'product':product[0]}
    return render(request,"detail.html",params)

def index2(request):
    return HttpResponse("Index shop tp")