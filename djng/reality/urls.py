from django.conf.urls import url, include
from . import views


from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)



app_name = 'reality'
urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^(?P<reality_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add, name='add'),
    url(r'^', include(router.urls)),
    url(r'^rest/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
