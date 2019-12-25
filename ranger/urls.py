from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('man',views.man,name='man'),
    path('calender', views.calender, name='calender'),
    path('<int:id>',views.tark, name='in'),
    path('in2/<int:id1>/<int:id>', views.tark2, name='mid'),
]
