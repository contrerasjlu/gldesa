# Powered by: Ing. Jorge Contreras
# Fecha: 23/08/2015

######################################################################
#  IMPORTANTE:                                                       #
#  Para definir una nueva vista, hay que verificar queel modelo este #
#  cargado en la importacion de modelos; si es una pagina interna se #
#  debe anteponer a la funcion el shorcut login_requiered y cargar el#
#  contexto basico con la funcion loadContext y enviarla a la vista.            #
######################################################################


from django.http import Http404,HttpResponseRedirect, HttpResponse

from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login, logout, user_logged_in

from django.contrib.auth.decorators import login_required

from .models import Client, Package, PackageType, menuOption

from django.shortcuts import render, get_object_or_404, get_list_or_404

from .forms import *

#Cargar el Menu
def loadMenu():
    m = menuOption.objects.all().order_by('order')
    return m

#Cualquier carga inicial de las vistas debe colocarse aca.
#Esta funcion debe ser cargada en cada inicio de vista interna
def loadContext(active):
    context = {}
    context['menu'] = loadMenu()
    context['active'] = active

    return context

#La funcion solo desconecta al usuario de la sesion
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('operator:auth'))

#################################################################
# Funcion Auth:                                                 #
# El metodo de autenticacion valida inicialmente si fue cargada #
# con un POST.                                                  #
# Si no viene por un POST muestra la vista de manera natural    #
# Si viene por un POST intenta autenticar el usuario            #
#################################################################
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
                msg = ["Invalid User o Password, please Try Again"] # TODO: Esto debe cambiarse a una tabla de mensajes
                c += 1 # Se Cuenta por si se requiere hacer algo con los Fail Attemps
                return render(request, 'galaxy_operator/auth.html', {'msg': msg})
        else:
            msg = ["Invalid User o Password, please Try Again"] #TODO: Esto debe cambiarse a una tabla de mensajes
            return render(request, 'galaxy_operator/auth.html', {'msg': msg})
    else:
        return render(request, 'galaxy_operator/auth.html')

#Pagina de Bienvenida a Galaxy Operator
@login_required(redirect_field_name='', login_url='operator:auth')
def index(request):
    context = loadContext('welcome')
    if request.user.is_authenticated():
        context['user'] = request.user
        return render(request, 'galaxy_operator/index.html', context)
    else:
        return HttpResponseRedirect(reverse('operator:auth'))

#Pagina para registrar un nuevo paquete
@login_required(redirect_field_name='', login_url='operator:auth')
def registerPackage(request):
    context = loadContext('register')
    if request.POST:
        try:
            client = Client.objects.get(email=request.POST['email'])
        except client.DoesNotExist:
            return render(request, 'galaxy_operator/register.html', context)
        context['client'] = client
        return render(request, 'galaxy_operator/register.html', context)
    else:
        return render(request, 'galaxy_operator/register.html', context)

#El metodo de Consulta de Paquetes valida inicialmente si fue cargada con un POST
#Si no viene por un POST muestra la vista solo con el formulario de consulta de tracking number
#Si viene por un POST intenta buscar el paquete y mostrar el detalle junto con las funciones adicionales
@login_required(redirect_field_name='', login_url='operator:auth')
def package(request):
    context = loadContext('track')
    if request.POST:
        try:
            pq = Package.objects.get(tracking=request.POST['tracking'])
        except Package.DoesNotExist:
            context['msg'] = "Package doesn't Exist" #TODO: Cargar el Mensaje desde el administrador de contenido
            return render(request, 'galaxy_operator/package.html', context)

        context['package'] = pq
        return render(request, 'galaxy_operator/package.html', context)
    else:
        return render(request, 'galaxy_operator/package.html', context)

@login_required(redirect_field_name='', login_url='operator:auth')
def client(request):
    context = loadContext('client')
    context['mytest'] = clientForm
    return render(request, 'galaxy_operator/client.html', context)