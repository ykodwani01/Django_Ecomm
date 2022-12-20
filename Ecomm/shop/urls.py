
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("checkout",views.checkout,name="checkout"),
    path("add",views.add,name='add'),
    path("cart",views.cart,name='cart'),
    path("profile",views.profile,name='profile'),
    

]
