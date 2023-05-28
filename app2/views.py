from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sweety(request):
    return render(request,'sweety.html')


def ooha(request):
    return HttpResponse('<h1>ooha navya sree</h1>')
