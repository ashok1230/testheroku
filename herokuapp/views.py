from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Home(request):
    return HttpResponse("Hi Ashok This is home page")

def Deep(request):
    return HttpResponse("Hi This is Deep Page")


