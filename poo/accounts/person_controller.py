from abc import ABCMeta, abstractclassmethod

from calificaciones.models import CalificacionTable
from .models import PersonaTable, Rol, Status
from calificaciones.calificacion_controller import Calificacion


# Abstract class
class Persona(metaclass=ABCMeta):
    """
    Abstract class
    Base of user and admin
    """
    def __init__(self):
        self._nombre = ''
        self._apellido = ''
        self._correo = ''
        self._fecha_nacimiento = ''
        self._rol = 2  # Client

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_apellido(self, apellido):
        self._apellido = apellido

    def set_correo(self, correo):
        self._correo = correo

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    def set_rol(self, rol):
        self._rol = rol

    def get_nombre(self):
        return self._nombre

    def get_apellido(self):
        return self._apellido

    def get_correo(self):
        return self._correo

    def get_fecha_nacimiento(self):
        return self._fecha_nacimiento

    def get_rol(self):
        return self._rol

    @abstractclassmethod
    def crear_usuario(self):
        pass

    @abstractclassmethod
    def cambiar_contrasena(self):
        pass

    @abstractclassmethod
    def find_rol(self):
        pass

    @abstractclassmethod
    def get_status(self):
        pass


class Usuario(Persona, Calificacion):

    def find_rol(self):
        rol = Rol.objects.get(id=self.get_rol())
        return rol

    def get_status(self):
        """
        Este metodo obtiene la instancia del modelo de status.
        por default el objeto con estado: activo
        """
        estado = Status.objects.get(status='Activo')
        return estado

    def crear_usuario(self):

        persona = PersonaTable(
            rol=self.find_rol(),
            first_name=self.get_nombre(),
            last_name=self.get_nombre(),
            email=self.get_correo(),
            fecha_nacimiento=self.get_fecha_nacimiento(),
            status=self.get_status()
        )
        try:
            ok = True
            response = persona.save()
        except Exception as e:
            ok = False
            response = 'Ha ocurrido un error: {} '.format(e)

        return ok, response

    def cambiar_contrasena(self):
        print("cambiar contrasena")

    def editar_perfil(self, id_usuario):
        """

        :param id_usuario:
        :return: ok, response
        """
        usuario = PersonaTable.objects.get(id=id_usuario)
        usuario.first_name = self.get_nombre()
        usuario.last_name = self.get_apellido()
        usuario.fecha_nacimiento = self.get_fecha_nacimiento()
        try:

            response = usuario.save()
            ok = True
        except Exception as e:
            ok = False
            response = 'Ha ocurrido un error: {}'.format(e)

        return ok, response

    def search_client(self, id_usuario):
        usuario = PersonaTable.objects.filter(id=id_usuario).last()
        return usuario

    def solicitar_creacion_lugar(self):
        pass

    def crear_comentario(self):
        pass

    def puntear_lugar(self):
        pass

    def subir_imagenes(self):
        pass

    def borrar_opiniones(self):
        pass

    def obtener_usuario(self, nombre):
        pass

    def calificar(self, id_usuario, score):

        usuario = PersonaTable.objects.get(id=id_usuario)
        calificaciones = CalificacionTable.objects.filter(tipo_calificacion='usuario')
        for calificacion in calificaciones:
            if calificacion.min_puntaje < score <= calificacion.max_puntaje:
                usuario.calificacion = calificacion


class Admin(Persona):
    _is_super_admin = False

    def find_rol(self):
        rol = Rol.objects.get(id=self.get_rol())
        return rol

    def is_super_admin(self, is_super_admin):
        __class__._is_super_admin = is_super_admin

    def get_status(self):
        """
        Este metodo obtiene la instancia del modelo de status.
        por default el objeto con estado: activo
        """
        estado = Status.objects.get(status='Activo')
        return estado

    def crear_usuario(self):
        print("crear usuario admin")
        persona = PersonaTable(
            rol=self.find_rol(),
            first_name=self.get_nombre(),
            last_name=self.get_nombre(),
            email=self.get_correo(),
            fecha_nacimiento=self.get_fecha_nacimiento(),
            status=self.get_status(),
            is_super_admin=__class__._is_super_admin
        )
        try:
            ok = True
            response = persona.save()
        except Exception as e:
            ok = False
            response = 'Ha ocurrido un error: {} '.format(e)

        return ok, response

    def cambiar_contrasena(self):
        print("cambiar contrasena admin")

    def aprobar_creacion_lugar(self, lugar, answer):

        pass

    def crear_categorias(self):

        pass

    def actualizar_categorias(self):
        pass

    def listar_usuarios(self):
        usuarios = PersonaTable.objects.all()
        return usuarios

