from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from app.models import *
import logging
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.db.models import Count

logger = logging.getLogger(__name__) 

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        logger.warning("form :", form)
        logger.warning("username: ", request.POST['username'])
        logger.warning("password: ", request.POST['password'])
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.get(username=form.cleaned_data.get('username'),
                                        password=form.cleaned_data.get('password'))
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return render(request, 'index.html')
    form = LoginForm()
    logger.warning("````````````````````````````````````````")
    return render(request, 'auth_form.html', {'form': form})

def base(request):
	news = News.objects.all()
	return render(request, 'index.html', {'news': news})

def about(request):
    return render(request, 'about.html')

def table(request, category):
    ad_list = Ad.objects.filter(category=category).annotate(complaint_count=Count('complaint'))
    return render(request, 'tables.html', {'category': category,'ad_list': ad_list})

def ad(request,ad_id):
	ad_info = get_object_or_404(Ad, id=ad_id)
	return render(request, 'ad.html',{'ad': ad_info})

def news(request,new_id):
	new_info = get_object_or_404(News, id=new_id)
	return render(request, 'news.html',{'news': new_info})

def registration_view(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        new_user.username = username
        new_user.set_password(password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('base'))
    context = {
        'form': form
    }
    return render(request, 'register_form.html', context)