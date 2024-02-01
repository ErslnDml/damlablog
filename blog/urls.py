from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_blog),
    path('homepage/', views.homepage_blog,name="homepage"),
    path('blogs/', views.blogs,name="blogs"),
    path('blogs/<slug:slug>', views.read,name="read_blog"),
    path('categories/', views.categories,name="categories"),
    path('categories/<slug:slug>', views.category_blog,name="category_blog"),
]