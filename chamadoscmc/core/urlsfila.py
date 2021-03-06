# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	url(r'^$', views.FilaChamadosIndexView.as_view(), name='index'),
	url(r'^api/chamados_atendente/(?P<usuario_id>[0-9]+)/(?P<status>[\w\-]+)/$', views.chamados_atendente_json, name='api-chamados-atendente'),
	url(r'^api/chamados_abertos/(?P<setor_id>[0-9]+)/$', views.chamados_abertos_json, name='api-chamados-abertos'),
	url(r'^api/chamados_estatistica/$', views.chamados_estatistica_json, name='api-chamados-estatistica'),
	url(r'^api/atende/(?P<id_chamado>[0-9]+)/$', views.atende_json, name='api-atende'),
	url(r'^api/devolve/(?P<id_chamado>[0-9]+)/$', views.devolve_json, name='api-devolve'),
	url(r'^api/reabre/(?P<id_chamado>[0-9]+)/$', views.reabre_json, name='api-reabre'),
	url(r'^api/respostas/(?P<id_chamado>[0-9]+)/$', views.respostas_json, name='api-respostas'),
	url(r'^atende/$', views.atende, name='atende'),
	url(r'^devolve/$', views.devolve, name='devolve'),
	url(r'^fecha/$', views.fecha, name='fecha'),
	url(r'^api/responde/$', views.responde_json, name='responde'),
]

