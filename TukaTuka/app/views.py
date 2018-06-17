from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from app.models import *
import logging
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from .forms import RegistrationForm, LoginForm, MailForm, FilterForm, AdForm, AdEditForm,EditDataForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict

logger = logging.getLogger(__name__) 

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        login_user = authenticate(username=username, password=password)
        if login_user:
            auth_login(request, login_user)
            return HttpResponseRedirect(reverse('base'))
    context = {
        'form': form
    }
    return render(request, 'auth_form.html', context)

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('base'))


def base(request):
    try:
        author_id=request.session['_auth_user_id']
        news = News.objects.all()
        form = MailForm(request.POST or None)
        if form.is_valid():
            new_mail = form.save(commit=False)
            email = form.cleaned_data['email']
            new_mail.email = email
            new_mail.save()
            return HttpResponseRedirect(reverse('base'))
        return render(request, 'index.html', {'news': news,'form': form,'author': author_id})
    except Exception as e:
        news = News.objects.all()
        form = MailForm(request.POST or None)
        if form.is_valid():
            new_mail = form.save(commit=False)
            email = form.cleaned_data['email']
            new_mail.email = email
            new_mail.save()
            return HttpResponseRedirect(reverse('base'))
        return render(request, 'index.html', {'news': news,'form': form})

def about(request):
    try:
        author_id=request.session['_auth_user_id']
        return render(request, 'about.html', {'author': author_id})
    except Exception as e:
        return render(request, 'about.html')

def donate(request):
    try:
        author_id=request.session['_auth_user_id']
        return render(request, 'donate.html', {'author': author_id})
    except Exception as e:
        return render(request, 'donate.html')

def table(request, category):
    try:
        author_id = request.session['_auth_user_id']
        ad_list = Ad.objects.filter(category=category).annotate(complaint_count=Count('complaint'))
        form = FilterForm(request.POST or None)
        if form.is_valid():
            categorys = form.cleaned_data['category1']
            ad_filter_list = Ad.objects.filter(category=category,category1=categorys)
            return render(request, 'table_filter.html', {'category': category,'ad_filter_list': ad_filter_list,'form': form})
        return render(request, 'tables.html', {'category': category,'ad_list': ad_list,'form': form, 'author': author_id})
    except Exception as e:
        ad_list = Ad.objects.filter(category=category).annotate(complaint_count=Count('complaint'))
        form = FilterForm(request.POST or None)
        if form.is_valid():
            categorys = form.cleaned_data['category1']
            ad_filter_list = Ad.objects.filter(category=category, category1=categorys)
            return render(request, 'table_filter.html',
                          {'category': category, 'ad_filter_list': ad_filter_list, 'form': form})
        return render(request, 'tables.html',
                      {'category': category, 'ad_list': ad_list, 'form': form})


def ad(request,ad_id):
    try:
        author_id = request.session['_auth_user_id']
        ad_info = get_object_or_404(Ad, id=ad_id)
        return render(request, 'ad.html',{'ad': ad_info, 'author': author_id})
    except Exception as e:
        ad_info = get_object_or_404(Ad, id=ad_id)
        return render(request, 'ad.html', {'ad': ad_info})


def news(request,new_id):
    try:
        author_id = request.session['_auth_user_id']
        new_info = get_object_or_404(News, id=new_id)
        form = MailForm(request.POST or None,auto_id=True)
        if form.is_valid():
            new_mail = form.save(commit=False)
            email = form.cleaned_data['email']
            new_mail.email = email
            new_mail.save()
            return HttpResponseRedirect(reverse('news'))
        return render(request, 'news.html',{'news': new_info,'form': form, 'author': author_id})
    except Exception as e:
        new_info = get_object_or_404(News, id=new_id)
        form = MailForm(request.POST or None, auto_id=True)
        if form.is_valid():
            new_mail = form.save(commit=False)
            email = form.cleaned_data['email']
            new_mail.email = email
            new_mail.save()
            return HttpResponseRedirect(reverse('news'))
        return render(request, 'news.html', {'news': new_info, 'form': form})

def registration_view(request):
    form = RegistrationForm(request.POST or None,auto_id=False)
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
            auth_login(request, login_user)
            return HttpResponseRedirect(reverse('base'))
    context = {
        'form': form
    }
    return render(request, 'register_form.html', context)
@login_required
def ad_form(request):
    form = AdForm(request.POST or None, request.FILES or None, auto_id=False)
    if form.is_valid():
        new_Ad = form.save(commit=False)
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        category = form.cleaned_data['category']
        company_adress = form.cleaned_data['company_adress']
        company_name = form.cleaned_data['company_name']
        name = form.cleaned_data['name']
        author_id = User.objects.get(id = request.session['_auth_user_id'])
        position = form.cleaned_data['position']
        phone_number = form.cleaned_data['phone_number']
        phone_another = form.cleaned_data['phone_another']
        price = form.cleaned_data['price']
        volume = form.cleaned_data['volume']
        photo = form.cleaned_data['photo']
        new_Ad.author = author_id
        new_Ad.title = title
        new_Ad.description = description
        new_Ad.category = category
        new_Ad.company_adress= company_adress
        new_Ad.company_name  = company_name
        new_Ad.name = name
        new_Ad.position = position
        new_Ad.phone_number = phone_number
        new_Ad.phone_another = phone_another
        new_Ad.price = price
        new_Ad.volume = volume
        new_Ad.photo = photo
        new_Ad.save()
        return HttpResponseRedirect(reverse('base'))
    context = {
        'form': form
    }
    return render(request, 'ad_form.html', context)
@login_required
def lichniy_kabinet(request):
    author_id = request.session['_auth_user_id']
    ad_list = Ad.objects.filter(author=author_id).annotate(author_count=Count('id'))
    return render(request, 'lk_objavi.html', {'ad_list': ad_list, 'author': author_id})
@login_required
def lichnaya_objava(request, ad_id):
    author_id = request.session['_auth_user_id']
    ad = Ad.objects.get(author=author_id, id=ad_id)
    form = AdEditForm(request.POST or None, request.FILES or None, initial=model_to_dict(ad), instance=ad, auto_id=False)
    if form.is_valid():
        new_Ad = form.save(commit=False)
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        category = form.cleaned_data['category']
        company_adress = form.cleaned_data['company_adress']
        company_name = form.cleaned_data['company_name']
        name = form.cleaned_data['name']
        author_id = User.objects.get(id = request.session['_auth_user_id'])
        position = form.cleaned_data['position']
        phone_number = form.cleaned_data['phone_number']
        phone_another = form.cleaned_data['phone_another']
        price = form.cleaned_data['price']
        volume = form.cleaned_data['volume']
        photo = form.cleaned_data['photo']
        new_Ad.author = author_id
        new_Ad.title = title
        new_Ad.description = description
        new_Ad.category = category
        new_Ad.company_adress= company_adress
        new_Ad.company_name  = company_name
        new_Ad.name = name
        new_Ad.position = position
        new_Ad.phone_number = phone_number
        new_Ad.phone_another = phone_another
        new_Ad.price = price
        new_Ad.volume = volume
        new_Ad.photo = photo
        new_Ad.save()
        return HttpResponseRedirect(reverse('lichniy-kabinet'))
    return render(request, 'ad_form.html', {'form': form})
@login_required
def delete_ad(request, ad_id):
    author_id = request.session['_auth_user_id']
    Ad.objects.get(author=author_id, id=ad_id).delete()
    return HttpResponseRedirect(reverse('lichniy-kabinet'))
@login_required
def lk_data(request):
    author_id = request.session['_auth_user_id']
    user_data = User.objects.get(id=author_id)
    form = EditDataForm(request.POST or None, initial=model_to_dict(user_data), instance=user_data, auto_id=False)
    if form.is_valid():
        edit_user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        edit_user.username = username
        edit_user.set_password(password)
        edit_user.first_name = first_name
        edit_user.last_name = last_name
        edit_user.save()
        login_user = authenticate(username=username, password=password)
        auth_login(request, login_user)
        return HttpResponseRedirect(reverse('lk_data'))
    return render(request, 'lk_data.html', {'form': form})
#def lichniy_cabinet_data(request, author):
  #  ad_list = Ad.objects.filter(author=author).annotate(author_count=Count('Objavleniy:'))
    #return render(request, 'lk_objavi.html', {'author': author})
