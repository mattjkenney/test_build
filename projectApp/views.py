from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .forms import TestForm
from .models import Test

# Create your views here.

def home(request):
    return render(request, "home.html")

def tests(request):
    if request.method == "POST":
        testForm = TestForm(request.POST, request.FILES)
        testForm.save()
    #elif "remove" in request.POST:
    #    Test.objects.get(request.get('to_remove')).delete()
    
    testForm = TestForm()
    context = {
        'testForm': testForm,
        'tests_current': Test.objects.all(),
        'tests_qty': Test.objects.count()
    }
    return render(request, "tests.html", context)

def parameters(request):
    return render(request, "parameters.html")

def criteria(request):
    return render(request, "criteria.html")

def builds(request):
    return render(request, "builds.html")
