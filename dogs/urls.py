from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<dog_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^update/', views.update, name='update'),
    url(r'^nearby/', views.all_nearby, name='all_nearby'),
]