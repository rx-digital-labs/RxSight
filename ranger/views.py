from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Count, Sum
from django.db.models.query import RawQuerySet
from django.db import connection

# Create your views here.

def index(request):
    return render(request,'ranger/index.html')