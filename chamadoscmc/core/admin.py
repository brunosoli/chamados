# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import GrupoServico, SetorChamado, Servico, Pavimento,  Localizacao

class GrupoServicoInline(admin.TabularInline):
	model = GrupoServico
	extra = 2
	verbose_name_plural = 'Grupos de Serviço'	

class ServicoInline(admin.TabularInline):
	model = Servico
	extra = 2
	verbose_name_plural = 'Serviços'		

class PavimentoInline(admin.TabularInline):
	model = Pavimento
	extra = 2
	verbose_name_plural = 'Pavimentos do Local'		

class SetorChamadoAdmin(admin.ModelAdmin):
	model = SetorChamado

	list_display = ('setor',)
	list_per_page = 20
	ordering = ('setor__set_nome', )
	search_fields = ('setor__set_nome', )
	inlines = [GrupoServicoInline]

class GrupoServicoAdmin(admin.ModelAdmin):
	model = GrupoServico
	list_filter = ['setor', ]
	ordering = ('descricao', )
	search_fields = ('descricao', )
	inlines = [ServicoInline]

class LocalizacaoAdmin(admin.ModelAdmin):
	model = Localizacao
	#list_filter = ['setor', ]
	ordering = ('descricao', )
	search_fields = ('descricao', )
	inlines = [PavimentoInline]	

admin.site.register(GrupoServico, GrupoServicoAdmin)
admin.site.register(SetorChamado, SetorChamadoAdmin)
admin.site.register(Localizacao, LocalizacaoAdmin)