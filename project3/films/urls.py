from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

app_name = 'films'

urlpatterns = [
    url(r'^$', views.film_list, name='film_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.film_list, name='film_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.film_detail, name='film_detail'),
    path('sign/', views.sign, name='sign'),
    url(r'^loging$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^loging/login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^loging/logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
]