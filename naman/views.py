from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import logging

logger = logging.getLogger('django.server')

def index(request):
    return HttpResponse("Hello, world. You're at the naman index.")

def delete(request):
    logger.info("USER DELETED")
    return HttpResponse("DELETED USER 1")


def index1(request):
    return HttpResponse(1/0)
