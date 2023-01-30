from django.contrib import admin
from api.models import Sobrevivente, Recursos, Itens, Infectado,Trocas
# Register your models here.

admin.site.register(Sobrevivente)
admin.site.register(Recursos)
admin.site.register(Itens)
admin.site.register(Infectado)
admin.site.register(Trocas)
