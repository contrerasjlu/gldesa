from django.http import Http404,HttpResponseRedirect, HttpResponse

from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login, logout, user_logged_in

from django.contrib.auth.decorators import login_required

from .models import Client, Package, PackageType

from django.shortcuts import render, get_object_or_404, get_list_or_404


@login_required(redirect_field_name='', login_url='operator:auth')
def index(request):
    if request.user.is_authenticated():
        return render(request, 'galaxy_operator/index.html', {'user': request.user})
    else:
        return HttpResponseRedirect(reverse('operator:auth'))

def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('operator:auth'))

#El metodo de autenticacion valida inicialmente si fue cargada con un POST
#Si no viene por un POST muestra la vista de manera natural
#Si viene por un POST intenta autenticar el usuario
def auth(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                #esta funcion es la que cambia la URL de la barra de navegacion
                return HttpResponseRedirect(reverse('operator:index'))
            else:
                msg = ["Invalid User o Password, please Try Again"] #Esto debe cambiarse a una tabla de mensajes
                c += 1
                return render(request, 'galaxy_operator/auth.html', {'msg': msg})
        else:
            msg = ["Invalid User o Password, please Try Again"] #Esto debe cambiarse a una tabla de mensajes
            return render(request, 'galaxy_operator/auth.html', {'msg': msg})
    else:
        return render(request, 'galaxy_operator/auth.html')

@login_required(redirect_field_name='', login_url='operator:auth')
def registerPackage(request):
    register = True
    return render(request, 'galaxy_operator/register.html', {'register':register})

def package(request):
    next()