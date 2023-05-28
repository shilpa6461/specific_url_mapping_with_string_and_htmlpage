from django.urls import path
from app2.views import *
app_name='pandu'

urlpatterns=[

    path('sweety/',sweety,name='sweety'),
    path('ooha/',ooha,name='ooha'),
]