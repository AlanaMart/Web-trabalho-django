from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'cidade', 'dataInicial', 'dataFinal', 'vagas', 'gratuito' )
    search_fields = ('titulo', 'cidade')
    list_filter = ('tipo', 'cidade', 'gratuito')
