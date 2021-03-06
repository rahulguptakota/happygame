from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/$', views.game, name='game'),
    url(r'^getimages/', views.getimages, name='getimages'),
    url(r'^sendinfo/', views.sendinfo, name='sendinfo'),
]