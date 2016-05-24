from django.conf.urls import url
from . import views


app_name = 'reality'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<reality_id>[0-9]+)/$', views.detail, name='detail'),
]