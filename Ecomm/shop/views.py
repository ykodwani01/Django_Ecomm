from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Orders
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
def searchMatch(query, item):
    if query in item.product_name or query in item.product_category:
        return True
    else:
        return False

def search(request):
    query= request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('product_category', 'id')
    cats = {item['product_category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(product_category=cat)
        prod=[item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds, "msg":""}
   
    return render(request, 'index.html', params)



def cart(request):
    # return render(request,"index.html")
    # js2py("console.log('hello');")
    # res_2 = js2py.eval_js(localStorage.getItem('cart'))
    # print(res_2)
    return render(request,"checkout.html")


def checkout(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        items_json=request.POST.get('items_address')
        order=Orders(name=name,email=email,address=address)
        order.save()
    return HttpResponse("index.html")
def add(request):
    return render(request,"index.html")
def profile(request):
    return render(request,"about.html")


def detail(request,myid):
    #fetching the product using id
    product=Product.objects.filter(id=myid)
    print(product)
    params={'product':product[0]}
    return render(request,"detail.html",params)

def index2(request):
    return HttpResponse("Index shop tp")