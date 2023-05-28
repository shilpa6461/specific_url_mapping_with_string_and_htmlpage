from django.urls import path
from app1.views import *
app_name='Nagaveni'



urlpatterns=[
    path('mummy/',mummy,name='mummy'),
    path('daddy/',daddy,name='daddy'),
    path('sasi/',sasi,name='sasi'),
]