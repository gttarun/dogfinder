from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<dog_name>[a-z]+)/$', views.detail, name='detail'),
    url(r'^(?P<dog_id>[0-9]+)/$', views.id_detail, name='id_detail'),
]