from .models import OpinionTable
from accounts.person_controller import Usuario
from calificaciones.calificacion_controller import Calificacion
from lugares.lugar_controller import Lugar


class Opinion(Calificacion):
    def __init__(self, lugar, persona):
        self._lugar  = lugar
        self._persona = persona
        # lugar_obj = Lugar()
        # self._lugar = lugar_obj.buscar_lugar(lugar_id)

        # persona_obj = Usuario()
        # self._usuario = persona_obj.search_client(persona_id)

    def agregar_opinion(self, opinion_description):
        opinion = OpinionTable(
            descripcion_opinion=opinion_description,
            lugar=self._lugar,
            usuario=self._usuario
        )
        opinion.save()

    def calificar(self, id_opinion, score):

        opinion = OpinionTable.objects.get(id=id_opinion)
        actual_score = opinion.puntaje

        opinion.puntaje = actual_score + score if actual_score + score > 0 else 0

        calificaciones = OpinionTable.objects.filter(tipo_calificacion='usuario')

        for calificacion in calificaciones:
            if calificacion.min_puntaje < opinion.puntaje <= calificacion.max_puntaje:
                opinion.calificacion = calificacion
                break

        opinion.save()







