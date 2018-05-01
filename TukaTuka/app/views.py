from django.shortcuts import render
from django.http import HttpResponse
from app.models import *


def base(request):
	news = list(News.objects.all())
	return render(request, 'index.html', {'news': news})

def about(request):
    return render(request, 'about.html')

def table(request):
    return render(request, 'tables.html')

def ad(request):
    return render(request, 'ad.html')
