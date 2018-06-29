from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_view
import django.urls
from .decorators import check_recaptcha

urlpatterns = [
 path('', views.base, name='base'),
 path('about', views.about, name='about'),
 path('donate', views.donate, name='donate'),
 path('sell/<int:category>-prodat-vtorsyre-na-pererabotku', views.table, name='sell'),
 path('buy/<int:category>-kupit-vtorsyre-na-pererabotku', views.table, name='buy'),
 path('buy_rec/<int:category>-kupit-pererabotannoe-syre', views.table, name='buy-rec'),
 path('sell_rec/<int:category>-prodat-pererabotannoe-syre', views.table, name='sell-rec'),
 path('<int:ad_id>-predlozheniya', views.ad, name='ad'),
 path('news/novost-<int:new_id>', views.news, name='news'),
 path('regist', check_recaptcha(views.registration_view), name='regist'),
 path('login', views.login_view, name='login'),
 path('logout', views.logout, name='logout'),
 path('lichniy-kabinet', views.lichniy_kabinet, name='lichniy-kabinet'),
 path('lichniy-kabinet/<int:ad_id>-objavlenie', views.lichnaya_objava, name='lichnaya_objava'),
 path('ad_form', views.ad_form, name='ad-form'),
 path('delete-<int:ad_id>', views.delete_ad, name='delete_ad'),
 path('lichniy-kabinet/data', views.lk_data, name='lk_data'),
 path('password-reset/',auth_view.PasswordResetView.as_view(), name='password_reset'),
 path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(), name='password_reset_done'),
 path('password-reset//reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
 path('password-reset/complete/', auth_view.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]