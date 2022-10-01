from .views import *
from django.urls import path

urlpatterns = [
    path('',index,name='home'),
    path('product/',product,name='product'),
    path('About/',aboutUs,name='about'),
    path('blog/',blog,name='blog'),
    path('contact/',contactUs,name='contact'),
]