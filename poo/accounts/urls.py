from __future__ import absolute_import

from django.conf.urls import url
from .views import crear_cliente, editar_perfil, crear_admin


urlpatterns = [

    # url(r'^listar$', listar_lugares, name='lugares_listar'),
    url(r'^crear$', crear_cliente, name='clientes_crear'),
    url(r'^crear_admin$', crear_admin, name='clientes_admin'),
    url(r'^editar/(?P<usuario_id>\d+)/$', editar_perfil, name='usuario_editar'),

]
