from accounts.models import PersonaTable
from calificaciones.models import CalificacionTable
from .models import LugarTable, Ciudad, Categoria
from calificaciones.calificacion_controller import Calificacion



class Lugar(Calificacion):
    """
    Clase Lugar
    """

    def __init__(self):
        self._id = ''
        self._nombre = ''
        self._ciudad = ''
        self._categoria = ''
        self._puntaje = ''
        self._created_by = ''

    def crear_lugar(self, data_lugar):
        """
        Crea objeto lugar y lo almacena en el modelo Lugar
        :return:
        """
        ok = False
        response = 'Ha occurrido un error'

        if data_lugar.is_valid():
            response = data_lugar.save()
            ok = True

        return ok, response

    def listar_lugares(self):
        """
        Retorna todos los lugares
        """

        lugar = LugarTable.objects.all()

        return lugar

    def buscar_lugar(self, id_lugar):
        print(id_lugar)
        lugar = LugarTable.objects.filter(id=id_lugar).last()
        return lugar

    def actualizar_lugar(self, data_lugar):
        """

        Retorna la data almacenada de actualizar lugar
        """
        ok = False
        response = 'Ha ocurrido un error'
        if data_lugar.is_valid():
            response = data_lugar.save()
            ok = True

        return ok, response

    def calificar(self, id_lugar, score):

        lugar = LugarTable.objects.get(id=id_lugar)
        actual_score = lugar.puntaje

        lugar.puntaje = actual_score + score if actual_score + score > 0 else 0

        calificaciones = CalificacionTable.objects.filter(tipo_calificacion='usuario')

        for calificacion in calificaciones:
            if calificacion.min_puntaje < lugar.puntaje <= calificacion.max_puntaje:
                lugar.calificacion = calificacion
                break

        lugar.save()


    def _preparar_data(self, ciudad, categoria, email):

        ciudad = Ciudad.objects.get(ciudad=ciudad)
        categoria = Categoria.objects.get(categoria=categoria)
        usuario = PersonaTable.objects.get(email=email)

        return ciudad, categoria, usuario



    def agregar_lugar(self, data_lugar):
        """
        Crea objeto lugar y lo almacena en el modelo Lugar
        :return:
        """
        ok = False
        response = 'Ha occurrido un error'

        print("lugar: ", data_lugar)
        ciudad, categoria, usuario = self._preparar_data(
            data_lugar.get('ciudad'),
            data_lugar.get('categoria'),
            data_lugar.get('usuario'))

        print(">>>>>>>>>", ciudad.id, categoria.id, usuario.id)

        lugar = LugarTable(
            nombre_lugar=data_lugar.get('nombre_lugar'),
            categoria=categoria,
            ciudad=ciudad,
            direccion=data_lugar.get('direccion'),
            puntaje=data_lugar.get('puntaje'),
            created_by=usuario)

        lugar.save()

        print("luuuuuu:", lugar.__dict__)

        return lugar

