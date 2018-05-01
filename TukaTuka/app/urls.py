from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.contrib.auth.views import LoginView
import django.urls
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
urlpatterns = [
 path('', views.base, name='base'),
 path('show1', views.show, name='show')
]