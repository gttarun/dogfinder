from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<dog_id>[0-9]+)/$', views.id_detail, name='id_detail'),
    url(r'^update/', views.update, name='update'),
    url(r'^nearby/', views.nearby, name='nearby'),
]