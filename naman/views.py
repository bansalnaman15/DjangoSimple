from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from request_logging.decorators import no_logging


def index(request):
    return HttpResponse("Hello, world. You're at the naman index.")