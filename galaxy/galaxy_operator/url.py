from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^auth/$', views.auth, name='auth'),
    url(r'^logout/$', views.userLogout, name='userLogout'),
    url(r'^register/$', views.registerPackage, name='register'),
    url(r'^(?P<pk>[0-9]+)/package/$', views.package, name='package'),

]
