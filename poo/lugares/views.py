from django.shortcuts import render, redirect
from .lugar_controller import Lugar
from .forms import LugarForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

from lugares.lugar_controller import Lugar
import json


# Create your views here.


def listar_lugares(request):

    lugar = Lugar()

    context = {'lugares': lugar.listar_lugares()}
    return render(request, 'lugares/lugares_listar.html', context)


def crear_lugares(request):

    if request.method == 'POST':
        form = LugarForm(request.POST)
        print(">>", request.POST)
        lugar = Lugar()
        ok, response = lugar.crear_lugar(form)
        if ok:
            return redirect('/lugares/listar')
        else:
            print(response)
            form = LugarForm()

    else:
        form = LugarForm()

        return render(request, 'lugares/lugares_crear.html', {'form': form})


def editar_lugar(request, lugar_id):
    """Renderiza la vista para editar. Instancia la clase y llama los metodos para editar."""

    lugar_instancia = Lugar()
    lugar = lugar_instancia.buscar_lugar(lugar_id)

    if request.method == 'GET':
        form = LugarForm(instance=lugar)
    else:
        form = LugarForm(request.POST, instance=lugar)
        ok, message = lugar_instancia.actualizar_lugar(form)
        if ok:
            return redirect('/lugares/listar')

    return render(request, 'lugares/lugares_crear.html', {'form': form})


class AgregarLugar(APIView):

    @classmethod
    def post(cls, request):
        print(">>>>>", request.data)

        lugar_instancia = Lugar()

        response = lugar_instancia.agregar_lugar(request.data)
        print("respuesta:", response)

        data = {
            "id": response.id,
            "nombre": response.nombre_lugar
        }
        status_code = status.HTTP_201_CREATED

        return Response(data=data, status=status_code)


class ListarLugar(APIView):

    @classmethod
    def get(cls, request, lugar_id):

        lugar_instancia = Lugar()

        response = lugar_instancia.buscar_lugar(lugar_id)
        print("respuesta:", response)

        data = {
            "id": response.id,
            "nombre": response.nombre_lugar,
            "direccion": response.direccion,
            "puntaje": response.puntaje
        }
        status_code = status.HTTP_201_CREATED

        return Response(data=data, status=status_code)
