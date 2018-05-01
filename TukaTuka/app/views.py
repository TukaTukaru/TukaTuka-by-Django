from django.shortcuts import render
from django.http import HttpResponse
from app.models import *


def base(request):
    return render(request, 'index.html')

def main(request):
    return render(request, 'index.html')

def table(request):
    return render(request, 'tables.html')

def ad(request):
    return render(request, 'ad.html')
