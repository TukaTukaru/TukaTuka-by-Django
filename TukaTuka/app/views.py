from django.shortcuts import render
from django.http import HttpResponse
from app.models import *


def base(request):
	news = News.objects.all()
	return render(request, 'index.html', {'news': news})

def about(request):
    return render(request, 'about.html')

def table(request, category):
    ad_list = Ad.objects.filter(category=category)
    return render(request, 'tables.html', {'category': category,'ad_list': ad_list})

def ad(request,ad_id):
	ad_info = Ad.objects.filter(id=ad_id)
	return render(request, 'ad.html',{'ad_info': ad_info})
