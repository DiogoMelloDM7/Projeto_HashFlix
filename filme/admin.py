from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin

#Só existe porque nós queremos que no admin apareça o campo personalizado filmes_vistos
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico",{"fields": ("filmes_vistos",)})
)
UserAdmin.fieldsets = tuple(campos)

#Registre seus modelos aqui
admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)
