from mongoengine import Document, EmbeddedDocument, fields
import time
from django.db.models import F


class Carreras(Document):
    id=fields.ObjectId
    temporada = fields.IntField(required=False)
    categoria = fields.StringField(required=False)
    abreviatura = fields.StringField(required=False)
    titulo = fields.StringField(required=False)
    lugar = fields.StringField(required=False)
    fecha = fields.DateTimeField(required=False)
    pos = fields.IntField(required=False)
    puntos = fields.IntField(required=False)
    num = fields.IntField(required=False)
    piloto = fields.StringField(required=False)
    pais = fields.StringField(required=False)
    equipo = fields.StringField(required=False)
    moto = fields.StringField(required=False)
    kmh = fields.FloatField(required=False)
    diferencia = fields.StringField(required=False)


class Campeonatos(Document):
    id=fields.ObjectId
    temporada = fields.IntField(required=False)
    categoria = fields.StringField(required=False)
    pos = fields.IntField(required=False)
    piloto = fields.StringField(required=False)
    moto = fields.StringField(required=False)
    pais = fields.StringField(required=False)
    puntos = fields.IntField(required=False)

class Documentacion(Document):
    id=fields.ObjectId
    temporada = fields.IntField(required=False)
    categoria = fields.StringField(required=False)
    abreviatura = fields.StringField(required=False)
    titulo = fields.StringField(required=False)
    lugar = fields.StringField(required=False)
    fecha = fields.StringField(required=False)
    documentacion = fields.ListField()

class Piloto(Document):
    #id=fields.ObjectId
    nombre = fields.StringField(required=False)
    pais = fields.StringField(required=False)
    wiki_piloto=fields.URLField(required=False) #Wikipedia
    foto_piloto=fields.URLField(required=False) #Wikipedia
    num_campeonatos_ganados=fields.StringField(required=False)
    datos_anuales=fields.ListField(required=False) #Año, V Media, Moto Usada, Posicion Campeonato, Carreras Ganadas

class PilotoRedirect(Document):
    nombre=fields.StringField(required=False)
    info=fields.StringField(required=False)

class Dashboard(Document):
    #id=fields.ObjectId
    #piloto_record_puntos_campeonato= fields.StringField(required=False)
    #piloto_mas_temporadas_corriendo= fields.StringField(required=False)
    #piloto_mas_puntos_historia= fields.StringField(required=False)
    #piloto_velocidad_media_mayor_carrera = fields.StringField(required=False)
    #nacionalidad_historica_pilotos=fields.ListField(required=False) 
    #moto_mas_victoriosa=fields.StringField(required=False)
    #ultima_carrera_disputada=fields.StringField(required=False)
    #resumen_ultima_carrera_disputada=fields.ListField(required=False)

    #####OtraAlternativa#####
    datos_historicos=fields.ListField(required=False)
    datos_ultima_temporada=fields.ListField(required=False)



