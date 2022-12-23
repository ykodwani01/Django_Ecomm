from django.shortcuts import render
from django.http import HttpResponse
from .models import post as Post
from blog.models import post
# from . import templates
# Create your views here.

def index(request):
    temp=Post.objects.all()
    print(temp)
    params={'posts': temp}
    return render(request,"index_blog.html",params)

def post(request,myid):
    temp=Post.objects.filter(post_id=myid)
    print(temp)
    params={'posts': temp[0]}   
    return render(request,'post.html',params)

def search(request):
    query=request.GET.get('query')
    posts=Post.objects.filter(title__icontains=query)
    params={ 'posts' : posts }
    return render(request,'search.html',params)