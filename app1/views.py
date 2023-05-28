from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mummy(request):
    return render(request,'mummy.html')


def daddy(request):
    return render(request,'daddy.html')

def sasi(request):
    return HttpResponse('<h1>sasi is an athletic</h1>')
