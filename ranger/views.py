from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Count, Sum
from django.db.models.query import RawQuerySet
from django.db import connection
from ranger.models import surgery, manpower, surR , ManR

# Create your views here.

def index(request):
    surg = surgery.objects.all()

    return render(request,'ranger/index.html',{'surg':surg})

def man(request):
    man = manpower.objects.all()

    return render(request,'ranger/the_manpower_page.html',{'man':man,'plea':plea})

def calender(request):
    return render(request,'ranger/calender.html')

#global 

def tark(request,id):
    man = manpower.objects.all()
    surg = surgery.objects.filter(pk=id).values('name')
    plea = surg[0].get('name')
    print(surg)
    q = surR(name=plea)
    q.save()
    #r = surR(name=surg,)
    return render(request, 'ranger/the_manpower_page.html', {'id': id,'man':man})

def tark2(request,id1,id):
    man = manpower.objects.filter(pk=id1).values('name')
    surg = surgery.objects.filter(pk=id).values('name')
    #plea = surg[0].get('name')
    print(man)
    lap = man[0].get('name')
    r = ManR(sid=id,name=lap)
    plea = surg[0].get('name')
    r.save()
    return render(request,'ranger/calender.html',{'lap':lap,'plea':plea})
