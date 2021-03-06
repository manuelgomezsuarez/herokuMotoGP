from django.shortcuts import render
from rest_framework_mongoengine import viewsets as meviewsets
from apiMotoGP.serializers import PosicionCarreraSerializer, PosicionCampeonatoSerializer, PosicionDocumentacionSerializer, PilotoSerializer, PilotoRedirectSerializer, DashboardSerializer
from app.models import Carreras, Campeonatos, Documentacion, Piloto, PilotoRedirect, Dashboard
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from django.template import loader
from rest_framework import filters, schemas, response
from rest_framework.utils.urls import remove_query_param, replace_query_param
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import AllowAny
import requests
import json
import re
import coreapi
from rest_framework.filters import BaseFilterBackend
import operator
from datetime import datetime



def index(request):
    template = loader.get_template('app/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


class carreraSwagger(BaseFilterBackend):
    def get_schema_fields(self, view):
        """
        'piloto', 'num','temporada','categoria','abreviatura','titulo','lugar','fecha','pos','puntos','pais','equipo','moto','kmh'
        """
        return [


            coreapi.Field(
                name='temporada',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='temporada__gt',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='temporada__lt',
                location='query',
                required=False,
                type='integer'
            ),


            coreapi.Field(
                name='temporada',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='temporada__gt',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='temporada__lt',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='piloto',
                location='query',
                required=False,
                type='string',
            ),
            coreapi.Field(
                name='piloto__icontains',
                location='query',
                required=False,
                type='string',
            ),

            coreapi.Field(
                name='num',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='num__gt',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='num__lt',
                location='query',
                required=False,
                type='integer'
            ),

            coreapi.Field(
                name='categoria',
                location='query',
                required=False,
                type='string'
            ),

            coreapi.Field(
                name='categoria__icontains',
                location='query',
                required=False,
                type='string'
            ),


            coreapi.Field(
                name='abreviatura',
                location='query',
                required=False,
                type='string'
            ),

            coreapi.Field(
                name='abreviatura__icontains',
                location='query',
                required=False,
                type='string'
            ),


            coreapi.Field(
                name='lugar',
                location='query',
                required=False,
                type='string'
            ),

            coreapi.Field(
                name='lugar__icontains',
                location='query',
                required=False,
                type='string'
            ),



            coreapi.Field(
                name='fecha',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='fecha__gt',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='fecha__lt',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='pais',
                location='query',
                required=False,
                type='string'
            ),

            coreapi.Field(
                name='pais__icontains',
                location='query',
                required=False,
                type='string'
            ),
            coreapi.Field(
                name='equipo',
                location='query',
                required=False,
                type='string'
            ),

            coreapi.Field(
                name='equipo__icontains',
                location='query',
                required=False,
                type='string'
            ),


            coreapi.Field(
                name='pos',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='pos__gt',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='pos__lt',
                location='query',
                required=False,
                type='integer'
            ),


            coreapi.Field(
                name='pos',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='pos__gt',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='pos__lt',
                location='query',
                required=False,
                type='integer'
            ),

            coreapi.Field(
                name='puntos',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='puntos__gt',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='puntos__lt',
                location='query',
                required=False,
                type='integer'
            ),

            coreapi.Field(
                name='kmh',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='kmh__gt',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='kmh__lt',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='titulo',
                location='query',
                required=False,
                type='string'
            ),

            coreapi.Field(
                name='titulo__icontains',
                location='query',
                required=False,
                type='string'
            ),



        ]

class campeonatoSwagger(BaseFilterBackend):
    def get_schema_fields(self, view):
        """
        'temporada','categoria','pos','piloto','moto','pais','puntos'
        """
        return [
            coreapi.Field(
                name='piloto',
                location='query',
                required=False,
                type='string',
            ),
            coreapi.Field(
                name='piloto__icontains',
                location='query',
                required=False,
                type='string',
            ),

            coreapi.Field(
                name='categoria',
                location='query',
                required=False,
                type='string'
            ),

            coreapi.Field(
                name='categoria__icontains',
                location='query',
                required=False,
                type='string'
            ),



            coreapi.Field(
                name='pos',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='pos__gt',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='pos__lt',
                location='query',
                required=False,
                type='integer'
            ),


            coreapi.Field(
                name='pos',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='pos__gt',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='pos__lt',
                location='query',
                required=False,
                type='integer'
            ),



            coreapi.Field(
                name='puntos',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='puntos__gt',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='puntos__lt',
                location='query',
                required=False,
                type='integer'
            ),

            coreapi.Field(
                name='temporada',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='temporada__gt',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='temporada__lt',
                location='query',
                required=False,
                type='integer'
            ),


            coreapi.Field(
                name='temporada',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='temporada__gt',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='temporada__lt',
                location='query',
                required=False,
                type='integer'
            ),

            coreapi.Field(
                name='moto',
                location='query',
                required=False,
                type='string',
            ),
            coreapi.Field(
                name='moto__icontains',
                location='query',
                required=False,
                type='string',
            ),


            coreapi.Field(
                name='pais',
                location='query',
                required=False,
                type='string',
            ),
            coreapi.Field(
                name='pais__icontains',
                location='query',
                required=False,
                type='string',
            ),



        ]

class pilotoSwagger(BaseFilterBackend):
    def get_schema_fields(self, view):
        """
        'nombre'
        """
        return [
            coreapi.Field(
                name='piloto',
                location='query',
                required=True,
                type='string',
            ),




        ]

class pilotoListSwagger(BaseFilterBackend):
    def get_schema_fields(self, view):
        """
        'nombre'
        """
        return [
            coreapi.Field(
                name='piloto',
                location='query',
                required=False,
                type='string',
            ),
            coreapi.Field(
                name='piloto__icontains',
                location='query',
                required=False,
                type='string',
            ),



        ]

class documentaccionSwagger(BaseFilterBackend):
    def get_schema_fields(self, view):
        """
        'temporada','categoria','abreviatura','titulo','lugar','fecha',
        """
        return [

            coreapi.Field(
                name='categoria',
                location='query',
                required=False,
                type='string'
            ),

            coreapi.Field(
                name='categoria__icontains',
                location='query',
                required=False,
                type='string'
            ),


            coreapi.Field(
                name='abreviatura',
                location='query',
                required=False,
                type='string'
            ),

            coreapi.Field(
                name='abreviatura__icontains',
                location='query',
                required=False,
                type='string'
            ),


            coreapi.Field(
                name='lugar',
                location='query',
                required=False,
                type='string'
            ),

            coreapi.Field(
                name='lugar__icontains',
                location='query',
                required=False,
                type='string'
            ),



            coreapi.Field(
                name='fecha',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='fecha__gt',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='fecha__lt',
                location='query',
                required=False,
                type='integer'
            ),


            coreapi.Field(
                name='titulo',
                location='query',
                required=False,
                type='string'
            ),

            coreapi.Field(
                name='titulo__icontains',
                location='query',
                required=False,
                type='string'
            ),


            coreapi.Field(
                name='temporada',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='temporada__gt',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='temporada__lt',
                location='query',
                required=False,
                type='integer'
            ),


            coreapi.Field(
                name='temporada',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='temporada__gt',
                location='query',
                required=False,
                type='integer'
            ),
            coreapi.Field(
                name='temporada__lt',
                location='query',
                required=False,
                type='integer'
            ),

        ]

class PosicionCarreraViewSet(meviewsets.ModelViewSet):
    """
    Listado de carreras.
    """
    serializer_class = PosicionCarreraSerializer
    filter_backends = (carreraSwagger,)

    def get_kwargs_for_filtering(self):
        filtering_kwargs = {}
        my_filter_fields = (
            'piloto',
            'num',
            'temporada',
            'categoria',
            'abreviatura',
            'titulo',
            'lugar',
            'fecha',
            'pos',
            'puntos',
            'pais',
            'equipo',
            'moto',
            'kmh')
        for field in self.request.query_params:  # Iteramos sobre los parámetros
            if field.split("__")[0] in my_filter_fields:
                field_value = self.request.query_params.get(field)
                if field_value:
                    filtering_kwargs[field] = field_value
        return filtering_kwargs

    def filter_queryset(self, queryset):
        return queryset

    def get_queryset(self):
        queryset = Carreras.objects.all().order_by('fecha')
        filtering_kwargs = self.get_kwargs_for_filtering()
        distinctUrl = self.request.query_params.get('distinct', None)
        if distinctUrl is not None:
            queryset = Carreras.objects.filter(
                **filtering_kwargs).order_by('fecha').distinct(distinctUrl)
            arrayQuerySet = []
            DictDistintos = {}
            for q in queryset:
                DictDistintos = ({distinctUrl: q})
                arrayQuerySet.append(DictDistintos)
            return arrayQuerySet
        else:
            if filtering_kwargs:
                queryset = Carreras.objects.filter(**filtering_kwargs)
            return queryset
    http_method_names = ['get']


class PosicionCampeonatoViewSet(meviewsets.ModelViewSet):
    """
    list:
    Listado de Campeonatos.
    """
    serializer_class = PosicionCampeonatoSerializer
    filter_backends = (campeonatoSwagger,)

    def get_kwargs_for_filtering(self):
        filtering_kwargs = {}
        my_filter_fields = (
            'temporada',
            'categoria',
            'pos',
            'piloto',
            'moto',
            'pais',
            'puntos')
        for field in self.request.query_params:  # iterate over the filter fields
            if field.split("__")[0] in my_filter_fields:
                # get the value of a field from request query parameter
                field_value = self.request.query_params.get(field)
                if field_value:
                    filtering_kwargs[field] = field_value
        return filtering_kwargs

    def get_queryset(self):
        queryset = Campeonatos.objects.all()
        # get the fields with values for filtering
        filtering_kwargs = self.get_kwargs_for_filtering()
        distinctUrl = self.request.query_params.get('distinct', None)
        if distinctUrl is not None:
            queryset = sorted(
                Campeonatos.objects.filter(
                    **filtering_kwargs).distinct(distinctUrl))  # filter the queryset based on
            arrayQuerySet = []
            DictDistintos = {}
            for q in queryset:
                DictDistintos = ({distinctUrl: q})
                arrayQuerySet.append(DictDistintos)
            return arrayQuerySet
        else:
            if filtering_kwargs:
                # filter the queryset based on 'filtering_kwargs'
                queryset = Campeonatos.objects.filter(**filtering_kwargs)
            return queryset
    def filter_queryset(self, queryset):
        return queryset
    http_method_names = ['get']


class PosicionDocumentacionViewSet(meviewsets.ModelViewSet):
    """
    list:
    Listado de Documentación.
    """
    serializer_class = PosicionDocumentacionSerializer
    filter_backends = (documentaccionSwagger,)

    def get_kwargs_for_filtering(self):
        filtering_kwargs = {}
        my_filter_fields = (
            'temporada',
            'categoria',
            'abreviatura',
            'titulo',
            'lugar',
            'fecha')
        for field in self.request.query_params:  # iterate over the filter fields
            if field.split("__")[0] in my_filter_fields:
                # get the value of a field from request query parameter
                field_value = self.request.query_params.get(field)
                if field_value:
                    filtering_kwargs[field] = field_value
        return filtering_kwargs

    def get_queryset(self):
        queryset = Documentacion.objects.all()
        # get the fields with values for filtering
        filtering_kwargs = self.get_kwargs_for_filtering()
        distinctUrl = self.request.query_params.get('distinct', None)
        if distinctUrl is not None:
            queryset = sorted(
                Documentacion.objects.filter(
                    **filtering_kwargs).distinct(distinctUrl))  # filter the queryset based on
            arrayQuerySet = []
            DictDistintos = {}
            for q in queryset:
                DictDistintos = ({distinctUrl: q})
                arrayQuerySet.append(DictDistintos)
            return arrayQuerySet
        else:
            if filtering_kwargs:
                # filter the queryset based on 'filtering_kwargs'
                queryset = Documentacion.objects.filter(**filtering_kwargs)
            return queryset

    def filter_queryset(self, queryset):
        return queryset
    http_method_names = ['get']


class PilotoViewSet(meviewsets.ModelViewSet):
    """
    list:
    Detalle de piloto.
    """
    serializer_class = PilotoSerializer
    filter_backends = (pilotoSwagger,)
    def get_kwargs_for_filtering(self):

        filtering_kwargs = {}
        my_filter_fields = ('piloto')
        for field in self.request.query_params:  # iterate over the filter fields
            if field.split("__")[0] in my_filter_fields:
                # get the value of a field from request query parameter
                field_value = self.request.query_params.get(field)
                if field_value:
                    filtering_kwargs[field] = field_value
        return filtering_kwargs

    
    def get_queryset(self):
        try:
            pilotos = []
            # get the fields with values for filtering
            filtering_kwargs = self.get_kwargs_for_filtering()
            try:
                urlWiki = requests.get(
                    "https://es.wikipedia.org/w/api.php?action=opensearch&search=" + (
                        filtering_kwargs.get('piloto')) + "&limit=1&format=json")
                resultWiki = urlWiki.json()

                urlWikiFoto = requests.get(
                    "https://en.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&prop=pageimages|pageterms&piprop=thumbnail&pithumbsize=200&titles=" +
                    resultWiki[1][0])

                resultWikiFoto = urlWikiFoto.json()
                infoPiloto = resultWiki[3][0]
                urls = re.findall(
                    r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                    str(resultWikiFoto))
                fotoPiloto = urls[0].replace("'", "").replace(",", "")
            except BaseException:

                fotoPiloto = "https://dit.ietcc.csic.es/wp-content/uploads/2018/11/foto-generica-200x200.jpg"
                infoPiloto = "Wiki Not Found"

            if filtering_kwargs:
                querysetCampeonato = Campeonatos.objects.all()
                querysetCarrera = Carreras.objects.all()
                query = querysetCampeonato.filter(
                    piloto=filtering_kwargs.get('piloto')).only(
                    'piloto', 'pais', 'pos').first()
                pilotos = []
                testPiloto = Piloto()
                testPiloto.nombre = query.piloto
                testPiloto.pais = query.pais
                testPiloto.wiki_piloto = infoPiloto
                testPiloto.foto_piloto = fotoPiloto
                pilotos = [testPiloto]
                p = testPiloto
                queryPiloto = querysetCampeonato.filter(
                    piloto=p.nombre).order_by('temporada').only(
                    'pos', 'temporada', 'moto', 'categoria')
                numCampeonatosGanados = querysetCampeonato.filter(
                    piloto=p.nombre, pos=1).count()
                p.num_campeonatos_ganados = int(numCampeonatosGanados) or 0
                cont = 0
                infoPiloto = Carreras._get_collection().aggregate([

                    {"$match": {"piloto": p.nombre}},


                    {
                        "$project": {
                            "kmh": "$kmh",
                            "temporada": "$temporada",
                            "categoria": "$categoria",
                            "moto": "$moto",
                            "equipo": "$equipo",
                            "puntos": "$puntos",
                            "victorias": {
                                "$cond": [{"$eq": ["$pos", 1]}, 1, 0]
                            },
                            "segundo": {
                                "$cond": [{"$eq": ["$pos", 2]}, 1, 0]
                            },

                            "tercero": {
                                "$cond": [{"$eq": ["$pos", 3]}, 1, 0]
                            },
                            "podios": {
                                "$cond": [{"$in": ["$pos", [1, 2, 3]]}, 1, 0]
                            }
                        }
                    },
                    {
                        "$group": {
                            "_id": {"temporada": "$temporada", "moto": "$moto", "categoria": "$categoria", "equipo": "$equipo"},
                            "victorias": {"$sum": "$victorias"},
                            "segundo": {"$sum": "$segundo"},
                            "tercero": {"$sum": "$tercero"},
                            "podios": {"$sum": "$podios"},
                            "vMedia": {"$avg": "$kmh"},
                            "sumPuntos": {"$sum": "$puntos"}
                        }
                    },
                    {"$sort": {"_id.temporada": 1}}

                ])

                puntosTemporada = Campeonatos._get_collection().aggregate([
                    {"$match": {"piloto": p.nombre}},


                    {
                        "$project": {
                            "pos": "$pos",
                            "temporada": "$temporada"
                        }
                    },
                    {
                        "$group": {
                            "_id": {"temporada": "$temporada", "pos": "$pos"}
                        }
                    },
                    {"$sort": {"_id.temporada": 1}},

                ])


    #            podios=Carreras._get_collection().aggregate([
    #            { "$match": { "pos":{"$lt":4},"piloto":testPiloto.nombre } },
    #            { "$group": {
    #                "_id": {"temporada":"$temporada"},
    #                "count": { "$sum": 1 }
    #            }}
    #        ])

                listaPuntosTemporada = list(puntosTemporada)
                for t in infoPiloto:
                    posicion = 0
                    #print("***Antes Del Bucle****")
                    # print(t.get("_id").get("temporada"))
                    # print("************************")

                    for punto in listaPuntosTemporada:
                        # print(punto.get("_id").get("temporada"))
                        if(punto.get("_id").get("temporada") == t.get("_id").get("temporada")):
                            posicion = punto.get("_id").get("pos")

                    # print(t.get("victorias"))
                    # print(t.get("podios"))
                    # print(t.get("vMedia"))
                    # campeonato_t=querysetCampeonato.filter(piloto=p.nombre,temporada=t.get("_id").get("temporada")).only('pos').first()
                    p.datos_anuales.append(
                        {
                            t.get("_id").get("temporada"): {
                                "categoria": t.get("_id").get("categoria"),
                                "moto": t.get("_id").get("moto"),
                                "num_victorias": t.get("victorias"),
                                "num_segundo": t.get("segundo"),
                                "num_tercero": t.get("tercero"),
                                "num_podios": t.get("podios"),
                                "posicion_campeonato": posicion,
                                "vel_media": t.get("vMedia"),
                                "url_campeonato": "https://motogp-api.herokuapp.com/campeonato/?temporada=" +
                                str(
                                    t.get("_id").get("temporada")) +
                                "&categoria=" +
                                t.get("_id").get("categoria")}})

                # for q in queryPiloto:

                #    cont=cont+1
                #    #vMedia=99999999.35
                #    #numVictorias=999999
                #    #numPodios=0
                #    vMedia=querysetCarrera.filter(piloto=filtering_kwargs.get('piloto'),temporada=q.temporada).average('kmh')
                #    numVictorias=querysetCarrera.filter(piloto=filtering_kwargs.get('piloto'),temporada=q.temporada,pos=1).count()
                #    numPodios=querysetCarrera.filter(piloto=filtering_kwargs.get('piloto'),temporada=q.temporada,pos__lt=4).count()

                #    p.datosAnuales.append({q.temporada:{
                #        "num_victorias":numVictorias,
                #        "num_podios":numPodios,
                #        "categoria":q.categoria,
                #        "velMedia":vMedia,
                #        "Moto":q.moto,
                #        "Posicion":q.pos}})
        except:
            pilotos=[]
        return pilotos

    def filter_queryset(self, queryset):
        return queryset

    http_method_names = ['get']


class PilotoRedirectViewSet(meviewsets.ModelViewSet):
    """
    list:
    Listado de Pilotos.
    """
    filter_backends = (pilotoListSwagger,)
    def get_kwargs_for_filtering(self):
        filtering_kwargs = {}
        my_filter_fields = ('piloto')
        for field in self.request.query_params:  # iterate over the filter fields
            if field.split("__")[0] in my_filter_fields:
                # get the value of a field from request query parameter
                field_value = self.request.query_params.get(field)
                if field_value:
                    filtering_kwargs[field] = field_value
        return filtering_kwargs

    serializer_class = PilotoRedirectSerializer
    def get_queryset(self):

        pilotos = []
        # get the fields with values for filtering
        filtering_kwargs = self.get_kwargs_for_filtering()
        query = Campeonatos.objects.filter(
            **filtering_kwargs).distinct('piloto')
        queryset = []
        for p in query:
            pil = PilotoRedirect()
            pil.nombre = p
            pil.info = "https://motogp-api.herokuapp.com/piloto/info/?piloto=" + \
                p.replace(" ", "%20")
            queryset.append(pil)

        return queryset

    def filter_queryset(self, queryset):
        return queryset
    http_method_names = ['get']


class DashboardViewSet(meviewsets.ModelViewSet):
    """
    list:
    Dashboard Histórico y Última Temporada.
    """

    def get_kwargs_for_filtering(self):
        filtering_kwargs = []
        return filtering_kwargs

    serializer_class = DashboardSerializer
    def get_queryset(self):

        dashboards = []
        # get the fields with values for filtering
        filtering_kwargs = self.get_kwargs_for_filtering()
        querysetCampeonato = Campeonatos._get_collection()
        querysetCarrera = Carreras._get_collection()
        topPuntosPilotos = []
        topPuntosPilotosCampeonato = []
        topCampeonatosDisputados = []
        topMotos = []
        topMotosTemporada = []
        dashboard = Dashboard()

        recordPuntosPiloto = querysetCampeonato.aggregate([
            {
                "$project": {
                    "piloto": "$piloto",
                    "puntos": "$puntos"
                }
            },
            {
                "$group": {
                    "_id": {"piloto": "$piloto", },
                    "puntos": {"$sum": "$puntos"},
                }
            },
            {"$sort": {"puntos": -1, }},
            {"$limit": 5},
        ])
        recordPuntosCampeonato = querysetCampeonato.aggregate([



            {
                "$project": {
                    "temporada": "$temporada",
                    "piloto": "$piloto",
                    "puntos": "$puntos"
                }
            },
            {
                "$group": {
                    "_id": {"piloto": "$piloto", "temporada": "$temporada"},
                    "puntos": {"$max": "$puntos"},
                }
            },
            {"$sort": {"puntos": -1, }},
            {"$limit": 5},

        ])

        recordVictoriasPiloto = querysetCarrera.aggregate([
            {
                "$project": {
                    "temporada": "$temporada",
                    "piloto": "$piloto",
                    "victorias": {
                        "$cond": [{"$eq": ["$pos", 1]}, 1, 0]
                    },
                }
            },
            {
                "$group": {
                    "_id": {"piloto": "$piloto", },
                    "victorias": {"$sum": "$victorias"},
                }
            },
            {"$sort": {"victorias": -1, }},
            {"$limit": 5},

        ])
        recordVictoriasPilotoCampeonato = querysetCampeonato.aggregate([
            {
                "$project": {
                    "temporada": "$temporada",
                    "piloto": "$piloto",
                    "victorias": {
                        "$cond": [{"$eq": ["$pos", 1]}, 1, 0]
                    },
                }
            },
            {
                "$group": {
                    "_id": {"piloto": "$piloto", },
                    "victorias": {"$sum": "$victorias"},
                }
            },
            {"$sort": {"victorias": -1, }},
            {"$limit": 5},

        ])

        recordCampeonatosDisputados = querysetCampeonato.aggregate([



            {
                "$project": {
                    "temporada": "$temporada",
                    "piloto": "$piloto",
                    "puntos": "$puntos"
                }
            },
            {
                "$group": {
                    "_id": {"piloto": "$piloto"},
                    "temporadas": {"$sum": 1},

                }
            },
            {"$sort": {"temporadas": -1, }},
            {"$limit": 5},

        ])
        recordMotosVictoriosas = querysetCarrera.aggregate([
            {
                "$project": {
                    "temporada": "$temporada",
                    "moto": "$moto",
                    "victorias": {
                        "$cond": [{"$eq": ["$pos", 1]}, 1, 0]
                    },
                }
            },
            {
                "$group": {
                    "_id": {"moto": "$moto", },
                    "victorias": {"$sum": "$victorias"},
                }
            },
            {"$sort": {"victorias": -1, }},
            {"$limit": 5},

        ])

        topVictoriasPiloto = []
        topVictoriasPilotoCampeonato = []
        for r in recordPuntosPiloto:
            topPuntosPilotos.append(
                {r.get("_id").get("piloto"): r.get("puntos")})
        for r in recordPuntosCampeonato:
            topPuntosPilotosCampeonato.append({r.get("_id").get(
                "piloto") + " - " + str(r.get("_id").get("temporada")): r.get("puntos")})
        for r in recordCampeonatosDisputados:
            topCampeonatosDisputados.append(
                {r.get("_id").get("piloto"): r.get("temporadas")})
        for r in recordMotosVictoriosas:
            topMotos.append({r.get("_id").get("moto"): r.get("victorias")})
        for r in recordVictoriasPiloto:
            topVictoriasPiloto.append(
                {r.get("_id").get("piloto"): r.get("victorias")})
        for r in recordVictoriasPilotoCampeonato:
            topVictoriasPilotoCampeonato.append(
                {r.get("_id").get("piloto"): r.get("victorias")})

        dashboard.datos_historicos.append(
            {"top5_victorias_carreras": topVictoriasPiloto})
        dashboard.datos_historicos.append(
            {"top5_victorias_campeonatos": topVictoriasPilotoCampeonato})
        dashboard.datos_historicos.append(
            {"top5_puntos_global": topPuntosPilotos})
        dashboard.datos_historicos.append(
            {"top5_puntos_temporada": topPuntosPilotosCampeonato})
        dashboard.datos_historicos.append(
            {"top5_campeonatos_disputados": topCampeonatosDisputados})
        dashboard.datos_historicos.append({"top5_victorias_marca": topMotos})

        ultimaCarrera = querysetCarrera.aggregate([
            {
                "$project": {
                    "fecha": "$fecha",
                    "temporada": "$temporada",
                    "titulo": "$titulo"
                }
            },
            {
                "$group": {
                    "_id": {"fecha": "$fecha", "temporada": "$temporada", "titulo": "$titulo"}
                }
            },
            {"$sort": {"_id.fecha": -1}},
            {"$limit": 1}

        ])
        ultimaTemporada = None
        for r in ultimaCarrera:
            ultimaTemporada = r.get("_id").get("temporada")
            dashboard.datos_ultima_temporada.append(
                {
                    "ultima_carrera": r.get("_id").get("fecha").strftime("%m/%d/%Y") +
                    " - " +
                    r.get("_id").get("titulo"),
                    "url_ultima_carrera": "https://motogp-api.herokuapp.com/carrera/" +
                    "?temporada=" +
                    str(ultimaTemporada) +
                    "&titulo=" +
                    r.get("_id").get("titulo").replace(
                        " ",
                        "%20")})
        numCarreras = len(
            Carreras.objects.filter(
                temporada=ultimaTemporada).distinct('titulo'))
        dashboard.datos_ultima_temporada.append(
            {"num_carreras_disputadas": numCarreras})

        recordMotosVictoriosasTemporada = querysetCarrera.aggregate([
            {"$match": {"temporada": ultimaTemporada}},

            {
                "$project": {
                    "temporada": "$temporada",
                    "categoria": "$categoria",
                    "moto": "$moto",
                    "victorias": {
                        "$cond": [{"$eq": ["$pos", 1]}, 1, 0]
                    },
                }
            },

            {
                "$group": {
                    "_id": {"moto": "$moto", "categoria": "$categoria"},
                    "victorias": {"$sum": "$victorias"},

                }
            },

            {"$sort": {"victorias": -1}},
            {
                "$group": {
                    "_id": "$_id.categoria",
                    "categoGroup": {
                        "$push": {
                            "moto": "$_id.moto",
                            "victorias": "$victorias"
                        }
                    },
                }
            },

        ])
        recordVictoriasPilotoTemporada = querysetCarrera.aggregate([
            {"$match": {"temporada": ultimaTemporada}},
            {
                "$project": {
                    "temporada": "$temporada",
                    "categoria": "$categoria",
                    "piloto": "$piloto",
                    "victorias": {
                        "$cond": [{"$eq": ["$pos", 1]}, 1, 0]
                    },
                }
            },

            {
                "$group": {
                    "_id": {"piloto": "$piloto", "categoria": "$categoria"},
                    "victorias": {"$sum": "$victorias"},

                }
            },

            {"$sort": {"victorias": -1}},
            {
                "$group": {
                    "_id": "$_id.categoria",
                    "categoGroup": {
                        "$push": {
                            "piloto": "$_id.piloto",
                            "victorias": "$victorias"
                        }
                    },
                }
            },

        ])
        topPilotosTemporada = []
        for r in recordVictoriasPilotoTemporada:
            topPilotosTemporada.append(
                {r.get("_id"): r.get("categoGroup")[:3]})
        dashboard.datos_ultima_temporada.append(
            {"top3_victorias": topPilotosTemporada})
        for r in recordMotosVictoriosasTemporada:
            topMotosTemporada.append({r.get("_id"): r.get("categoGroup")[:3]})
        dashboard.datos_ultima_temporada.append(
            {"top3_victorias_marca": topMotosTemporada})
        nacionalidadPilotos = querysetCampeonato.aggregate([

            {"$match": {"temporada": ultimaTemporada}},

            {
                "$project": {
                    "temporada": "$temporada",
                    "categoria": "$categoria",
                    "piloto": "$piloto",
                    "pais": "$pais",

                }
            },

            {
                "$group": {
                    "_id": {"temporada": "$temporada", "categoria": "$categoria", "pais": "$pais"},
                    "suma": {"$sum": 1},

                }
            },
            {"$sort": {"suma": -1, }},

            {
                "$group": {
                    "_id": "$_id.categoria",
                    "categoGroup": {
                        "$push": {
                            "pais": "$_id.pais",
                            "total": "$suma"
                        }
                    },
                }
            },

        ])

        nacionalidadPilotosList = []
        for r in nacionalidadPilotos:
            nacionalidadPilotosList.append(
                {r.get("_id"): r.get("categoGroup")})
        dashboard.datos_ultima_temporada.append(
            {"nacionalidad_pilotos": nacionalidadPilotosList})
        dashboards = [dashboard]
        return dashboards
    http_method_names = ['get']
