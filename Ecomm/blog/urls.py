
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="BlogHome"),
    # path("tp",views.index2,name="tp")
    path("post/<int:myid>",views.post,name="post"),
    path("search",views.search,name="search")
]
