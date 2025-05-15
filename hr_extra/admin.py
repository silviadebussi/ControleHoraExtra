from django.contrib import admin

from .models import Fiscal, Administrador, Hora_extra, Dia_da_semana

admin.site.register(Fiscal)
admin.site.register(Administrador)
admin.site.register(Hora_extra)
admin.site.register(Dia_da_semana)