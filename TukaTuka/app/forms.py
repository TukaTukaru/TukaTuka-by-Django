from django import forms
from django.contrib.auth.models import User
from app.models import Mail, Ad

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_check = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']
        widgets = {
        'username' : forms.EmailInput(attrs={'placeholder' : 'Ваша почта'}),
        'first_name' : forms.TextInput(attrs={'placeholder' : 'Имя', 'name' : 'Name'}),
        'last_name' : forms.TextInput(attrs={'placeholder' : 'Фамилия', 'name' : 'Surname'}),
        'password' : forms.PasswordInput(attrs={'placeholder' : 'Пароль', 'name' : 'pass'}),
        'password_check' : forms.PasswordInput(attrs={'placeholder' : 'Повторите пароль', 'name' : 'pass'}),
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
            fields = ['title', 'description', 'category', 'company_adress', 'company_name', 'name', 'position', 'phone_number', 'phone_another', 'price', 'volume', 'photo']
            widgets = {
                'title': forms.TextInput(attrs={'placeholder': 'Название продукта'}),
                'description': forms.Textarea(attrs={'placeholder': 'Описание продукта'}),
                'category': forms.RadioSelect(attrs={'placeholder': 'Я хочу'}),
                'company_adress': forms.TextInput(attrs={'placeholder': 'Фактический адрес(город, улица, дом)'}),
                'company_name': forms.TextInput(attrs={'placeholder': 'Название организации'}),
                'name': forms.TextInput(attrs={'placeholder': 'Ф.И.О представителя'}),
                'position': forms.TextInput(attrs={'placeholder': 'Должность'}),
                'phone_number': forms.NumberInput(attrs={'placeholder': 'Ваш номер телефона', 'type' : 'tel'}),
                'phone_another': forms.NumberInput(attrs={'placeholder': 'Дополнительный номер', 'type' : 'tel'}),
                'price': forms.NumberInput(attrs={'placeholder': 'Цена, руб/тонна'}),
                'volume': forms.NumberInput(attrs={'placeholder': 'Объем, тонн'}),
                'photo': forms.FileInput(attrs={'placeholder': 'Фото продукции'}),
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


class FilterForm(forms.Form):
    category1 = forms.TypedChoiceField(choices = (
        (1, "ПП"),
        (2, "ПНД"),
        (3, "ПВД"),
        (4, "Стрейч"),
        (5, "ПЭТ"),
        (6, "Другое"),),
    coerce=int,empty_value=1
    )
    # volume = forms.IntegerField()
    # price = forms.IntegerField()

    
    # def clean(self):
    #     username = self.cleaned_data['username']
    #     password = self.cleaned_data['password']
    #     if not User.objects.filter(username=username).exists():
    #         raise forms.ValidationError('User with this login has not already registered')

    #     user = User.objects.get(username=username)
    #     if user and not user.check_password(password):
    #         raise forms.ValidationError('Пароль неверный!')
