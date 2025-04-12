from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is how you customise Welcome page into plain boring one.")


    