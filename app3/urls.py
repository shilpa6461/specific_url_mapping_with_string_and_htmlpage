from django.urls import path
from app3.views import *
app_name='nobitha'

urlpatterns=[
    path('nikki/',nikki,name='nikki'),
    path('akka/',akka,name='akka'),
]