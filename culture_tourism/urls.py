from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^main/(?P<pk>\d+)/$', views.mainarticle, name='mainarticle'),
    url(r'^menus/(?P<pk>\d+)/$', views.menu, name='menu'),
    url(r'small/(?P<pk>\d+)', views.small_to_big, name='small'),
    url(r'news/(?P<pk>\d+)/$', views.news, name='news'),
    url(r'most-visited/(?P<pk>\d+)/$', views.most_visited, name='most_visited'),
    url(r'feedback/$', views.feedback, name='feedback'),
    url(r'search/$', views.search, name='search'),
    url(r'adiblar/$', views.adiblar, name='adiblar'),
    url(r'maqollar/$', views.maqollar, name='maqollar'),
    url(r'about/$', views.about_us, name='about'),
    url(r'regions/', views.regions, name='regions'),
    url(r'region/(?P<pk>\d+)/$', views.regions, name='regions'),
    url(r'gallery/', views.gallery, name='gallery'),
    url(r'library/', views.library, name='library'),
    url(r'tales/', views.tales, name='tales'),

]
