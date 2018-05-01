from django.shortcuts import render
from django.http import HttpResponse
from app.models import *


def base(request):
    return render(request, 'index.html')

def show(request):
    return HttpResponse("Hello, World, r")

