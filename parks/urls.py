from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<park_name>[A-Za-z]+)/$', views.detail, name='detail'),
]