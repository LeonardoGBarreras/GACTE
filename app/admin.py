from django.contrib import admin

from .models import Evento,CrearEvento
# Register your models here.
class EventoAdmin (admin.ModelAdmin):
    list_display =("nombre","lugar","fecha","requisitos","transporte")
    list_editable = ("lugar","fecha","requisitos","transporte")
    search_fields =("nombre","lugar")


admin.site.register (Evento,EventoAdmin)
admin.site.register (CrearEvento)