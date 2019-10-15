from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addshow$', views.addshow),
    url(r'^shows/(?P<id>\d+)$', views.showdetails),
    url(r'^shows$', views.mainshowpage),
    url(r'^shows/(?P<id>\d+)/destroy$', views.destroy),
    url(r'^shows/(?P<id>\d+)/edit$', views.editshow),
    url(r'^shows/(?P<id>\d+)/update$', views.updateshow),
]