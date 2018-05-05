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
 path('sell/<int:category>-prodat-vtorsyre-na-pererabotku', views.table, name='sell'),
 path('buy/<int:category>-kupit-vtorsyre-na-pererabotku', views.table, name='buy'),
 path('buy_rec/<int:category>-kupit-pererabotannoe-syre', views.table, name='buy-rec'),
 path('sell_rec/<int:category>-prodat-pererabotannoe-syre', views.table, name='sell-rec'),
 path('predlozheniya-<int:ad_id>', views.ad, name='ad')
]