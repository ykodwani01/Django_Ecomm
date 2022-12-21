
from django.contrib import admin
from django.urls import path
import js2py
from . import views
urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("checkout",views.checkout,name="checkout"),
    path("cart",views.cart,name='cart'),
    path("profile",views.profile,name='profile'),
    path("search",views.search,name='search'),
    path("detail/<int:myid>",views.detail,name='detail'),
    

]
