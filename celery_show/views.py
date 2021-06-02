from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .tasks import sleepy


def index(request):
    sleepy.delay(10)
    return HttpResponse("Hello index")
