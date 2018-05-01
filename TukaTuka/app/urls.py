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
 path('about', views.about, name='about'),
 path('sell', views.table, name='sell'),
 path('buy', views.table, name='buy'),
 path('buy_rec', views.table, name='buy_rec'),
 path('sell_rec', views.table, name='sell_rec')
]