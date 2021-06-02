from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .tasks import sleepy,send_mail_task


def index(request):
    #sleepy.delay(10)
    send_mail_task()
    return HttpResponse("Hello  email")
