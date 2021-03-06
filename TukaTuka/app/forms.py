from django import forms
from django.contrib.auth.models import User
from app.models import Mail, Ad,Proposal
from django_filters.filters import CharFilter, ChoiceFilter
import django_filters
from django.db import models
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget

class RegistrationForm(forms.ModelForm):
    password_check = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Повторите пароль', 'name' : 'password_check'}))
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']
        widgets = {
        'username' : forms.EmailInput(attrs={'placeholder' : 'Ваша почта'}),
        'first_name' : forms.TextInput(attrs={'placeholder' : 'Имя', 'name' : 'Name'}),
        'last_name' : forms.TextInput(attrs={'placeholder' : 'Фамилия', 'name' : 'Surname'}),
        'password' : forms.PasswordInput(attrs={'placeholder' : 'Пароль', 'name' : 'pass'}),
    
        }
        help_texts = {
            'username': (''),
        }
        error_messages = {
            'username': {
                'max_length': ("Превышена длинна"),
            },
        }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Обязательно'
        self.fields['password'].label = 'Пароль'
        self.fields['password_check'].label = 'Повторите пароль'
        self.fields['first_name'].label = 'Введите'
        self.fields['last_name'].label = "Введите"

    def clean(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с такой почтой уже зарегистрирован')
        password_check = self.cleaned_data['password_check']
        password = self.cleaned_data['password']
        if password_check!=password:
            raise forms.ValidationError('Пароль не совпадает!')

class EditDataForm(RegistrationForm):

    def clean(self):
        password_check = self.cleaned_data['password_check']
        password = self.cleaned_data['password']
        if password_check!=password:
            raise forms.ValidationError('Пароль не совпадает!')

class MailForm(forms.ModelForm):

    class Meta:
        model = Mail
        fields = ["email"]
        widgets = {
        'email' : forms.EmailInput(attrs={'placeholder' : 'Введите E-mail', 'name' : 'email'}),
        }

class AdForm(forms.ModelForm):

    class Meta:
            model = Ad
            fields = ['title', 'description', 'category', 'category1', 'category2', 'company_adress', 'company_name', 'name', 'position', 'phone_number', 'phone_another', 'price', 'volume', 'photo',]
            widgets = {
                'title': forms.TextInput(attrs={'placeholder': 'Название продукта'}),
                'description': forms.Textarea(attrs={'placeholder': 'Описание продукта', 'rows' : '2'}),
                'category': forms.RadioSelect(attrs={'placeholder': 'Я хочу'}),
                'company_adress': forms.TextInput(attrs={'placeholder': 'Фактический адрес (город, улица, дом)'}),
                'company_name': forms.TextInput(attrs={'placeholder': 'Название организации'}),
                'name': forms.TextInput(attrs={'placeholder': 'Ф.И.О представителя'}),
                'position': forms.TextInput(attrs={'placeholder': 'Должность'}),
                'phone_number': forms.NumberInput(attrs={'placeholder': 'Ваш номер телефона', 'type' : 'tel'}),
                'phone_another': forms.NumberInput(attrs={'placeholder': 'Дополнительный номер(необязательно)', 'type' : 'tel'}),
                'price': forms.NumberInput(attrs={'placeholder': 'Цена, руб/тонна'}),
                'volume': forms.NumberInput(attrs={'placeholder': 'Объем, тонн'}),
                'photo': forms.ClearableFileInput(attrs={'placeholder': 'Фото продукции'}),
            }

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.EmailInput(attrs={'name' : 'log', 'id' : 'user_login', 'class' : 'input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'name' : 'pwd', 'id' : 'user_pass', 'class' : 'input'}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('User with this login has not already registered')

        user = User.objects.get(username=username)
        if user and not user.check_password(password):
            raise forms.ValidationError('Пароль неверный!')


class FilterForm(django_filters.FilterSet):
    CATEGORY_CHOICES=  ((1, "ПП"),
        (2, "ПНД"),
        (3, "ПВД"),
        (4, "Стрейч"),
        (5, "ПЭТ"),
        (6, "Другое"),)
    CATEGORY_GRANULE = (
        (1, "Гранула ПП"),
        (2, "Гранула ПНД"),
        (3, "Гранула ПВД"),
        (4, "Гранула стрейч"),
        (5, "Другое"),
    )
    category1 = ChoiceFilter(widget=forms.RadioSelect,
                                  choices=CATEGORY_CHOICES,
empty_label=None)
    category2 = ChoiceFilter(widget=forms.RadioSelect,
                                  choices=CATEGORY_GRANULE,
empty_label=None)
    price = django_filters.NumberFilter()
    price_min = django_filters.NumberFilter(name='price', lookup_expr='gte',widget=forms.NumberInput(attrs={'placeholder': 'От'}))
    price_max = django_filters.NumberFilter(name='price', lookup_expr='lte',widget=forms.NumberInput(attrs={'placeholder': 'До'}))
    volume = django_filters.NumberFilter()
    volume_min = django_filters.NumberFilter(name='volume', lookup_expr='gte',widget=forms.NumberInput(attrs={'placeholder': 'От'}))
    volume_max = django_filters.NumberFilter(name='volume', lookup_expr='lte',widget=forms.NumberInput(attrs={'placeholder': 'До'}))
    class Meta:
            model = Ad
            fields = ['price','volume','category1','category2']
            

    

    
   

class AdEditForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = ['title', 'description', 'category', 'company_adress', 'company_name', 'name', 'position', 'phone_number', 'phone_another', 'price', 'volume', 'photo',]
        widgets = {
                'title': forms.TextInput(),
                'description': forms.Textarea(attrs={'rows' : '2'}),
                'category': forms.RadioSelect(),
                'company_adress': forms.TextInput(),
                'company_name': forms.TextInput(),
                'name': forms.TextInput(),
                'position': forms.TextInput(),
                'phone_number': forms.NumberInput({'type' : 'tel'}),
                'phone_another': forms.NumberInput({'type' : 'tel'}),
                'price': forms.NumberInput(),
                'volume': forms.NumberInput(),
                'photo': forms.ClearableFileInput(),
                }
class ProposalForm(forms.ModelForm):

    class Meta:
            model = Proposal
            fields = [ 'description',  'name', 'phone_number', 'price','email']
            widgets = {
                'email' : forms.EmailInput(attrs={'placeholder' : 'mycompany@co.com'}),
                'description': forms.Textarea(attrs={'placeholder': 'Требуется стрейч пленка с загрязнением не более 3%. Прессованная в тюки.', 'rows' : '1'}),
                'name': forms.TextInput(attrs={'placeholder': 'Сегрей Иванов'}),
                'phone_number': PhoneNumberInternationalFallbackWidget(attrs={'placeholder': '+7 (925) 115 32 83'}),
                'price': forms.NumberInput(attrs={'placeholder': '27 рублей/кг'}),
                
            }
