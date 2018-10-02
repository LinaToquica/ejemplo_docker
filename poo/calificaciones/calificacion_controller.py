from abc import ABCMeta, abstractclassmethod


class Calificacion(metaclass=ABCMeta):
    """
    INTERFACE CALIFICACION
    """
    @abstractclassmethod
    def calificar(self, id_calificable, score):
        pass


