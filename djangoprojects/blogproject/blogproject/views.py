import django.http
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def publish(request):
    return render(request, 'publish.html')

