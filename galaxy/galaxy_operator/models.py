# Creado por: Ing. Jorge Contreras
# Fecha: 23/08/2015

from django.db import models

from django.contrib.auth.models import User

# Primero: Las clases son tablas que son creadas en la Base de Datos de la App

# Esta clase es creada para manejar los tipos de paquetes disponibles en la aplicacion Ej: Sobre, Caja
class PackageType(models.Model):
    name = models.CharField(max_length=10)	
    description = models.CharField(max_length=500)
    def __unicode__(self):
        return self.name

# Esta clase es creada para manejar los tipos de atributos de un paquete en particular, 
# solo deben crearse para cuando el tipo de paquete no comparta los mismos atributos con 
# el resto, es decir, no lo pueda almacenar el objeto 'Paquete' por si solo.

class PackageTypeAttribute(models.Model):
    ATTR_TYPE = (('I', 'Integer'),('V', 'Varchar'),)
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    attributeType = models.CharField(max_length=1, choices=ATTR_TYPE)
    packageType = models.ForeignKey(PackageType)
    def __unicode__(self):
        return self.name

# Localizaciones de los paquetes y estados de la ruta de un paquete.
class Location(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=250)
    address = models.TextField(max_length=250)
    zipCode = models.IntegerField()
    def __unicode__(self):
        return self.name

# Maestro de Rutas de la aplicacion
class Route(models.Model):
    code = models.CharField(max_length=45)
    description = models.TextField(max_length=250)
    def __unicode__(self):
        return self.code

# Estados de un paquete
class State(models.Model):
    STATE_TYPES = (('IN', 'Recibed'),('OUT', 'Delivered'),
                   ) 
    code = models.CharField(max_length=45)
    description = models.TextField(max_length=250)
    stateType = models.CharField(max_length=3, choices=STATE_TYPES)
    location = models.ForeignKey(Location)
    def __unicode__(self):
        return self.code

# Entradas de un cambio de estado
class StateAttribute(models.Model):
    ATTR_TYPE = (('I', 'Integer'),('V', 'Varchar'),)
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    attributeType = models.CharField(max_length=1, choices=ATTR_TYPE)
    state = models.ForeignKey(State)
    def __unicode__(self):
        return self.name

class Client(models.Model):
    STATES = (
        ('AL','Alabama'),('AK','Alaska'),('AZ','Arizona'),
        ('AR','Arkansas'),('CA','California'),('NC','North Caroline'),
        ('SC','South Caroline'),('CO','Colorado'),('CT','Connecticut'),
        ('ND','North Dakota'),('SD','South Dakota'),('DE','Delaware'),
        ('FL','Florida'),('GA','Giorgia'),('HI','Hawaii'),('ID','Idaho'),
        ('IL','Illinois'),('IN','Indiana'),('IA','Iowa'),('KS','Kansas'),
        ('KY','Kentucky'),('LA','Luisiana'),('ME','Maine'),('MD','Maryland'),
        ('MA','Massachusetts'),('MI','Michigan'),('MN','Minesota'),('MS','Mississippi'),
        ('MO','Missouri'),('MT','Montana'),('NE','Nebraska'),('NV','Nevada'),
        ('NJ','New Jersey'),('NY','New York'),('NH','New Hampshire'),('NW','New Mexico'),
        ('OH','Ohio'),('OK','Oklahoma'),('OR','Oregon'),('PA','Pennsylvania'),
        ('RI','Rhode Island '),('TN','Tennessee'),('TX','Texas'),('UT','Utah'),
        ('VT','Vermont'),('VA','Virginia'),('WA','Washington'),('WI','Wisconsin'),
        ('WY','Wyoming'),
    )
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50,default='Atlanta')
    state = models.CharField(max_length=2, choices=STATES, default='GA')
    country = models.CharField(max_length=3, default='USA')
    zip = models.IntegerField()
    telephone = models.CharField(max_length=20)
    email = models.EmailField(default='@')
    def __unicode__(self):
        return self.name

# Maestro de Paquetes
class Package(models.Model):
    content = models.TextField(max_length=250)
    origin = models.ForeignKey(Location)
    route = models.ForeignKey(Route)
    operator = models.ForeignKey(User)
    value = models.IntegerField()
    packageType = models.ForeignKey(PackageType)
    client = models.ForeignKey(Client, default=1)
    tracking = models.CharField(max_length=17)
    currentState = models.ForeignKey(State)
    def __unicode__(self):
        return self.tracking

# Valores de las entradas de un cambio de estado
class StateDetail(models.Model):
    attribute = models.ForeignKey(StateAttribute)
    package = models.ForeignKey(Package)
    value = models.CharField(max_length=250)
    def __unicode__(self):
        return self.attribute

# En esta clase se define la ruta de un paquete
class PackagesRoute(models.Model):
    route = models.ForeignKey(Route)
    state = models.ForeignKey(State)
    order = models.IntegerField()
    def __unicode__(self):
        return self.route

class PackageDetail(models.Model):
    attribute = models.ForeignKey(PackageTypeAttribute)
    package = models.ForeignKey(Package)
    value = models.CharField(max_length=250)
    def __unicode__(self):
        return self.attribute

class OutType(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    def __unicode__(self):
        return self.name

class StateAction(models.Model):
    out_type = models.ForeignKey(OutType)
    state = models.ForeignKey(State)
    def __unicode__(self):
        return self.out_type

class menuOption(models.Model):
    label = models.CharField(max_length=50)
    order = models.IntegerField()
    def __unicode__(self):
        return self.label

class GenericVars(models.Model):
    code = models.CharField(max_length=17)
    description = models.TextField()
    value = models.CharField(max_length=50)

class level(models.Model):
    name = models.CharField(max_length=50)
    share = models.DecimalField(decimal_places=2, max_digits=4)

#Este es el complemento del objeto User que viene por defecto con Django
class AgentDetail(models.Model):
    STATES = (
        ('AL','Alabama'),('AK','Alaska'),('AZ','Arizona'),
        ('AR','Arkansas'),('CA','California'),('NC','North Caroline'),
        ('SC','South Caroline'),('CO','Colorado'),('CT','Connecticut'),
        ('ND','North Dakota'),('SD','South Dakota'),('DE','Delaware'),
        ('FL','Florida'),('GA','Giorgia'),('HI','Hawaii'),('ID','Idaho'),
        ('IL','Illinois'),('IN','Indiana'),('IA','Iowa'),('KS','Kansas'),
        ('KY','Kentucky'),('LA','Luisiana'),('ME','Maine'),('MD','Maryland'),
        ('MA','Massachusetts'),('MI','Michigan'),('MN','Minesota'),('MS','Mississippi'),
        ('MO','Missouri'),('MT','Montana'),('NE','Nebraska'),('NV','Nevada'),
        ('NJ','New Jersey'),('NY','New York'),('NH','New Hampshire'),('NW','New Mexico'),
        ('OH','Ohio'),('OK','Oklahoma'),('OR','Oregon'),('PA','Pennsylvania'),
        ('RI','Rhode Island '),('TN','Tennessee'),('TX','Texas'),('UT','Utah'),
        ('VT','Vermont'),('VA','Virginia'),('WA','Washington'),('WI','Wisconsin'),
        ('WY','Wyoming'),
    )
    prevAgent = models.ForeignKey(User)
    birth = models.DateField()
    ssoTax = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50,default='Atlanta')
    state = models.CharField(max_length=2, choices=STATES, default='GA')
    zip = models.IntegerField()
    telephone = models.CharField(max_length=20)
    bank = models.CharField(max_length=20)
    bankAcct = models.CharField(max_length=50)
    level = models.ForeignKey(level)

class network(models.Model):
    agent = models.ForeignKey(User)
    refered = models.ForeignKey(AgentDetail)
    recla = models.DateField()