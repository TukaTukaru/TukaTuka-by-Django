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
 path('<int:ad_id>-predlozheniya', views.ad, name='ad'),
 path('news/novost-<int:new_id>', views.news, name='news'),
 path('regist', views.registration_view, name='regist'),
 path('login', views.login_view, name='login'),
 path('logout', views.logout, name='logout'),
]