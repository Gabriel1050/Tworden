from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return HttpResponse("<h1>WELCOME<h1>")
def login(request):
    return render(request, 'paginas/login.html')