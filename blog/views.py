from django.shortcuts import render
from .models import Category,Blog

def homepage_blog(request):
    data={
        "category":Category.objects.all(),
        "blog":Blog.objects.all()
    }
    return render(request,"blogs/home.html",data)
def blogs(request):
    data={
        "category":Category.objects.all(),
        "blog":Blog.objects.all()
    }
    return render(request,"blogs/blogs.html",data)
def categories(request):
    data={
        "category":Category.objects.all(),
        "blog":Blog.objects.all()
    }
    return render(request,"blogs/categories.html",data)

def category_blog(request,slug):
    data={
        "category":Category.objects.all(),
        "blog":Blog.objects.filter(active=True,category__slug=slug)
    }
    return render(request,"blogs/categories.html",data)

def read(request,slug):
    data={
        "id":Blog.objects.get(slug=slug),
        "blog":Blog.objects.all()
    }
    return render(request,"blogs/read.html",data)