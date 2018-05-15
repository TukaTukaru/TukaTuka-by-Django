from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput,label_suffix='')
    password_check = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'password_check', 'first_name', 'last_name']
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

class SignupForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, help_text='Обязательно')
    last_name = forms.CharField(max_length=30, help_text='Обязательно')
    email = forms.EmailField(max_length=254, help_text='Обязательно. Введите корректный email.')

    class Meta:
        fields = ("username", "password", "email", "first_name", "last_name")
        model = User


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

        