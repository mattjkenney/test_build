from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "home.html")

def tests(request):
    return render(request, "tests.html")

def parameters(request):
    return render(request, "parameters.html")

def criteria(request):
    return render(request, "criteria.html")

def builds(request):
    return render(request, "builds.html")