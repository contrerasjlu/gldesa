from django.contrib import admin

from .models import *

admin.site.register(PackageType)

admin.site.register(PackageTypeAttribute)

admin.site.register(Location)

admin.site.register(Route)
    
admin.site.register(State)

admin.site.register(StateAttribute)
    
admin.site.register(Package)

admin.site.register(StateDetail)

admin.site.register(PackagesRoute)

admin.site.register(PackageDetail)

admin.site.register(OutType)

admin.site.register(StateAction)

admin.site.register(Client)

admin.site.register(menuOption)

admin.site.register(GenericVars)

admin.site.register(level)

admin.site.register(AgentDetail)

admin.site.register(network)