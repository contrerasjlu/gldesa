from django.conf.urls import url

from . import views

urlpatterns = [
    #Pagina principal del GalaxyOperator
    url(r'^$', views.index, name='index'),

    #Pagina de Login
    url(r'^auth/$', views.auth, name='auth'),

    #Pagina pibote de logout
    url(r'^logout/$', views.userLogout, name='userLogout'),

    #Pagina para registrar un nuevo paquete
    url(r'^register/$', views.registerPackage, name='register'),

    #Pagina para registrar un nuevo Cliente
    url(r'^client/$', views.client, name='client'),

    #Pagina para consultar un paquete
    url(r'^package/$', views.package, name='package'),
]
