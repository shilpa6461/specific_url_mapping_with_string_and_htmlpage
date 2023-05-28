from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def nikki(request):
    return render(request,'nikki.html')

def akka(request):
    return HttpResponse('<h1>Premalatha</h1>')
