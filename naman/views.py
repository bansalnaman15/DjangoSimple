from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the naman index.")

def index1(request):
    return HttpResponse(1/0)
