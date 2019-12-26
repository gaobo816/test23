"""test23 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.template import loader
# from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import redirect
def yimi(request):
    return HttpResponse('hello yimi')

def subdir(request):
    # with open("templates/yimi.html","r",encoding="utf-8") as f:
    #     data=f.read()
    # return HttpResponse(data)
    return render(request,"yimi.html")

def index(request):

    print("----------")

    # print(request.POST)
    nameurl=request.POST.get("lname")

    with open('data.txt','a+') as f:
        f.write(nameurl)
        f.write('\n')

    # return HttpResponse('hello index')
    return HttpResponseRedirect("http://newpower.io:9999/")


urlpatterns = [
    path('admin/', yimi),
    path('subdir/', subdir),
    path('index/', index),
]
