from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('manpower',views.manpower,name='manpower'),
]
