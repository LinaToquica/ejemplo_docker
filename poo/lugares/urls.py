from __future__ import absolute_import

from django.conf.urls import url
from .views import listar_lugares, crear_lugares, editar_lugar, AgregarLugar, ListarLugar

urlpatterns = [

    url(r'^listar$', listar_lugares, name='lugares_listar'),
    url(r'^crear$', crear_lugares, name='lugares_crear'),
    url(r'^editar/(?P<lugar_id>\d+)/$', editar_lugar, name='lugar_editar'),
    url(r'^API_crear/$', AgregarLugar.as_view(), name='Add_lugar'),
    url(
        r'^buscar/(?P<lugar_id>\d+)/$',
        ListarLugar.as_view(),
        name='listar lugar'
    ),


]
