from django.conf.urls import patterns, url
from teaching import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^search/$', views.searching, name='search'),)