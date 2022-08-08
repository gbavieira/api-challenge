from django.contrib import admin
from .models import Receita, Despesa

class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id','descricao','data',)
    list_display_links = ('id','descricao')
    search_fields = ('descricao','data')
    list_per_page = 30


class ListandoDespesas(admin.ModelAdmin):
    list_display = ('id','descricao','data',)
    list_display_links = ('id','descricao')
    search_fields = ('descricao','data')
    list_per_page = 30

admin.site.register(Receita, ListandoReceitas)
admin.site.register(Despesa, ListandoDespesas)
