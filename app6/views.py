from django.shortcuts import render,redirect
from django.http import HttpResponse
from app6.models import gymInfo

# Create your views here.

def index(request):
    return render(request,'index.html')

def product(request):
    return render(request,'product.html')

def aboutUs(request):
    return render(request,'About_us.html')

def blog(request):
    return render(request,'blog.html')

def contactUs(request):
    if request.method == 'POST':
        # name = print(request.POST.get('name1'))
        # email = print(request.POST.get('email1'))
        # service = print(request.POST.get('service1'))
        # msg = print(request.POST.get('msg1'))

        name = request.POST.get('name1')
        email = request.POST.get('email1')
        service = request.POST.get('service1')
        msg = request.POST.get('msg1')
        gymData = gymInfo.objects.create(Name=name,Email=email,Msg=msg,Service=service)
        # print(gymData)
        return redirect('contact')


    return render(request,'contact_us.html')
