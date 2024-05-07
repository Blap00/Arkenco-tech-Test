from django.contrib import admin

from .models import *
# Register your models here.

# Vista ADMIN
admin.site.register(Usuarios)
admin.site.register(cliente)

# Vista USUARIO
admin.site.register(estado)
admin.site.register(etapa)
admin.site.register(prospecto)
