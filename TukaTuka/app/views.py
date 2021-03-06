from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from app.models import *
import logging
import json
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from .forms import RegistrationForm, LoginForm, MailForm, FilterForm, AdForm, AdEditForm,EditDataForm,ProposalForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.core.mail import send_mail



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
    form = ProposalForm(request.POST or None)
    if form.is_valid():
        new_mail = form.save()
        new_mail.save()
        send_mail(
    'Новый клиент',
    f'{new_mail.name} {new_mail.phone_number} {new_mail.description} {new_mail.price}.',
    'sultanovelutingol@yandex.ru',
    ['ponomarevgeorge@yandex.ru'],
    fail_silently=False,
)
        return HttpResponseRedirect(reverse('base'))
    return render(request, 'index.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def test_index(request):
    return render(request, 'test_index.html')

def test_about(request):
    return render(request, 'test_about.html')

def test_buy(request):
    return render(request, 'test_buy.html')

def test_sell(request):
    return render(request, 'test_sell.html')

def map(request):
    adresses = Ad.objects.all()
    lists_adress = [i.company_adress for i in adresses]
    filepath = 'static/assets/list.json'
    with open(filepath, 'w') as block_file:
        json.dump(lists_adress, block_file, ensure_ascii = False)
    return render(request, 'map.html')

def donate(request):
    return render(request, 'donate.html')

def table(request, category):
    ad_list = Ad.objects.filter(category=category)
    filtr = FilterForm(request.GET, queryset=ad_list)
#     if form.is_valid():
#         if form.cleaned_data['price_max']:    
#             ad_list = Ad.objects.filter(category=category,price__lte=form.cleaned_data['price_max'])
#         if form.cleaned_data['volume_min']:
#             ad_list = Ad.objects.filter(category=category,volume__gte=form.cleaned_data['volume_min'])
#         if form.cleaned_data['volume_max']:    
#             ad_list = Ad.objects.filter(category=category,volume__lte=form.cleaned_data['volume_max'])
#         if form.cleaned_data['price_min'] or form.cleaned_data['price_max'] or form.cleaned_data['volume_min'] or form.cleaned_data['volume_max']:
#             ad_list = Ad.objects.filter(category=category,price__gte=form.cleaned_data['price_min'],price__lte=form.cleaned_data['price_max']
# ,volume__gte=form.cleaned_data['volume_min']
# ,volume__lte=form.cleaned_data['volume_max'])
    return render(request, 'tables.html',
                      {'category': category, 'ad_list': ad_list, 'filtr': filtr})


def ad(request,ad_id):
    ad_info = get_object_or_404(Ad, id=ad_id)
    return render(request, 'ad.html', {'ad': ad_info})


def news(request,new_id):
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
        if request.recaptcha_is_valid:
            new_user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email=form.cleaned_data['username']
            new_user.email = email
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
        return HttpResponseRedirect(reverse('lichniy-kabinet'))
    context = {
        'form': form
    }
    return render(request, 'ad_form.html', context)
@login_required
def lichniy_kabinet(request):
    author_id = request.session['_auth_user_id']
    ad_list = Ad.objects.filter(author=author_id).annotate(ad_count=Count('id'))
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
