from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Count, Sum
from django.db.models.query import RawQuerySet
from django.db import connection
from ranger.models import surgery, manpower

# Create your views here.

def index(request):
    surg = surgery.objects.all()

    return render(request,'ranger/index.html',{'surg':surg})

def man(request):
    man = manpower.objects.all()

    return render(request,'ranger/the_manpower_page.html',{'man':man})

def calender(request):
    return render(request,'ranger/calender.html')

def tark(request,id):
    surg = surgery.objects.filter(pk=id).values('name')
    plea = surg[0].get('name')
    print(plea)
    return render(request,'ranger/calender.html')