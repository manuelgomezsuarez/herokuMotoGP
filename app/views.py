from django.shortcuts import render
from rest_framework_mongoengine import viewsets as meviewsets
from apiMotoGP.serializers import PosicionCarreraSerializer, PosicionCampeonatoSerializer,PosicionDocumentacionSerializer,PilotoSerializer,PilotoRedirectSerializer
from app.models import  Carreras, Campeonatos,Documentacion,Piloto,PilotoRedirect
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from django.template import loader
from rest_framework import filters,schemas,response
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

def index(request):
    template = loader.get_template('app/index.html')
    context = {
      
    }
    return HttpResponse(template.render(context,request))


class SimpleFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        """
        'piloto', 'num','temporada','categoria','abreviatura','titulo','lugar','fecha','pos','puntos','pais','equipo','moto','kmh'
        """
        return [
            coreapi.Field(
            name='piloto',
            location='query',
            required=False,
            type='string',
            description='Filtra por piloto'
        ),
                coreapi.Field(
            name='piloto__icontains',
            location='query',
            required=False,
            type='string',
            description='Filtra por contenido en piloto sin distinción entre mayúsculas y minúsculas'
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
                
                
                
                
                ]

class PosicionCarreraViewSet(meviewsets.ModelViewSet):
    """
    Listado de carreras.
    """
    serializer_class = PosicionCarreraSerializer
    filter_backends = (SimpleFilterBackend,)
    def get_kwargs_for_filtering(self):
        filtering_kwargs = {} 
        my_filter_fields = ('piloto', 'num','temporada','categoria','abreviatura','titulo','lugar','fecha','pos','puntos','pais','equipo','moto','kmh')
        for field in  self.request.query_params: # iterate over the filter fields
            if field.split("__")[0] in my_filter_fields:
                field_value = self.request.query_params.get(field) # get the value of a field from request query parameter
                if field_value: 
                    filtering_kwargs[field] = field_value
        return filtering_kwargs 

    def filter_queryset(self,queryset):
        return queryset
    def get_queryset(self):
        queryset = Carreras.objects.all().order_by('fecha')
        filtering_kwargs = self.get_kwargs_for_filtering() # get the fields with values for filtering 
        distinctUrl= self.request.query_params.get('distinct', None)
        if distinctUrl is not None:
            queryset = Carreras.objects.filter(**filtering_kwargs).order_by('fecha').distinct(distinctUrl) # filter the queryset based on
            arrayQuerySet=[]
            DictDistintos={}
            for q in queryset:
                DictDistintos=({distinctUrl:q})
                arrayQuerySet.append(DictDistintos)
            return arrayQuerySet
        else:
            if filtering_kwargs:
                queryset = Carreras.objects.filter(**filtering_kwargs) # filter the queryset based on 'filtering_kwargs'
            return queryset
    http_method_names = ['get']




class PosicionCampeonatoViewSet(meviewsets.ModelViewSet):
    """
    list:
    Listado de Campeonatos.
    """
    serializer_class = PosicionCampeonatoSerializer

    def get_kwargs_for_filtering(self):
        filtering_kwargs = {} 
        my_filter_fields = ('temporada', 'categoria','pos','piloto','moto','pais','puntos')
        for field in  self.request.query_params: # iterate over the filter fields
            if field.split("__")[0] in my_filter_fields:
                field_value = self.request.query_params.get(field) # get the value of a field from request query parameter
                if field_value: 
                    filtering_kwargs[field] = field_value
        return filtering_kwargs 

    def get_queryset(self):
        queryset = Campeonatos.objects.all()
        filtering_kwargs = self.get_kwargs_for_filtering() # get the fields with values for filtering 
        distinctUrl= self.request.query_params.get('distinct', None)
        if distinctUrl is not None:
            queryset = Campeonatos.objects.filter(**filtering_kwargs).distinct(distinctUrl) # filter the queryset based on
            queryset.sort()
            arrayQuerySet=[]
            DictDistintos={}
            for q in queryset:
                DictDistintos=({distinctUrl:q})
                arrayQuerySet.append(DictDistintos)
            return arrayQuerySet
        else:
            if filtering_kwargs:
                queryset = Campeonatos.objects.filter(**filtering_kwargs) # filter the queryset based on 'filtering_kwargs'
            return queryset
    http_method_names = ['get']


class PosicionDocumentacionViewSet(meviewsets.ModelViewSet):
    """
    list:
    Listado de Documentación.
    """
    serializer_class = PosicionDocumentacionSerializer

    def get_kwargs_for_filtering(self):
        filtering_kwargs = {} 
        my_filter_fields = ('temporada', 'categoria','abreviatura','titulo','lugar','fecha')
        for field in  self.request.query_params: # iterate over the filter fields
            if field.split("__")[0] in my_filter_fields:
                field_value = self.request.query_params.get(field) # get the value of a field from request query parameter
                if field_value: 
                    filtering_kwargs[field] = field_value
        return filtering_kwargs 

    def get_queryset(self):
        queryset = Documentacion.objects.all() 
        filtering_kwargs = self.get_kwargs_for_filtering() # get the fields with values for filtering 
        distinctUrl= self.request.query_params.get('distinct', None)
        if distinctUrl is not None:
            queryset = Documentacion.objects.filter(**filtering_kwargs).distinct(distinctUrl) # filter the queryset based on
            queryset.sort()
            arrayQuerySet=[]
            DictDistintos={}
            for q in queryset:
                DictDistintos=({distinctUrl:q})
                arrayQuerySet.append(DictDistintos)
            return arrayQuerySet
        else:
            if filtering_kwargs:
                queryset = Documentacion.objects.filter(**filtering_kwargs) # filter the queryset based on 'filtering_kwargs'
            return queryset
    http_method_names = ['get']




class PilotoViewSet(meviewsets.ModelViewSet):
    """
    list:
    Listado de Pilotos.
    """

    def get_kwargs_for_filtering(self):
 
        filtering_kwargs = {} 
        my_filter_fields = ('piloto')
        for field in  self.request.query_params: # iterate over the filter fields
            if field.split("__")[0] in my_filter_fields:
                field_value = self.request.query_params.get(field) # get the value of a field from request query parameter
                if field_value: 
                    filtering_kwargs[field] = field_value
        return filtering_kwargs 
    
    serializer_class = PilotoSerializer
    def get_queryset(self):
        
        pilotos=[]
        filtering_kwargs = self.get_kwargs_for_filtering() # get the fields with values for filtering 
        try:
            urlWiki = requests.get("https://es.wikipedia.org/w/api.php?action=opensearch&search="+(filtering_kwargs.get('piloto'))+"&limit=1&format=json")
            resultWiki = urlWiki.json()

            urlWikiFoto=requests.get("https://en.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&prop=pageimages|pageterms&piprop=thumbnail&pithumbsize=200&titles="+resultWiki[1][0])

            resultWikiFoto=urlWikiFoto.json()
            infoPiloto=resultWiki[3][0]
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(resultWikiFoto))
            fotoPiloto=urls[0].replace("'","").replace(",","")
        except:

            fotoPiloto="https://dit.ietcc.csic.es/wp-content/uploads/2018/11/foto-generica-200x200.jpg"
            infoPiloto="Wiki Not Found"


        if filtering_kwargs:
            querysetCampeonato=Campeonatos.objects.all()
            querysetCarrera=Carreras.objects.all()
            query=querysetCampeonato.filter(piloto=filtering_kwargs.get('piloto')).only('piloto','pais','pos').first()
            pilotos=[]
            testPiloto= Piloto()
            testPiloto.nombre=query.piloto
            testPiloto.pais=query.pais
            testPiloto.infoPiloto=infoPiloto
            testPiloto.fotoPiloto=fotoPiloto
            pilotos=[testPiloto]
            p=testPiloto
            queryPiloto=querysetCampeonato.filter(piloto=p.nombre).order_by('temporada').only('pos','temporada','moto','categoria')
            numCampeonatosGanados=querysetCampeonato.filter(piloto=p.nombre,pos=1).count()
            p.numCampeonatosGanados=int(numCampeonatosGanados) or 0;
            cont=0
            infoPiloto=Carreras._get_collection().aggregate([
                    
                { "$match": { "piloto":p.nombre} },


    {
        "$project": {
            "kmh":"$kmh",
            "temporada": "$temporada",
            "categoria": "$categoria",
            "moto": "$moto",
            "equipo": "$equipo",
            "victorias": {  
                "$cond": [ { "$eq": ["$pos", 1 ] }, 1, 0]
            },
            "podios": {  
                "$cond": [ { "$in": [ "$pos", [1,2,3] ] }, 1, 0]
            }
        }
    },
    {
        "$group": {
            "_id": {"temporada":"$temporada","moto":"$moto","categoria":"$categoria"},
            "victorias": { "$sum": "$victorias" },
            "podios": { "$sum": "$podios" },
            "vMedia":{"$avg":"$kmh"}
        }
    },
    {"$sort":{"_id.temporada":1}}

])

            puntosTemporada=Campeonatos._get_collection().aggregate([
                { "$match": { "piloto":p.nombre} },


    {
        "$project": {
            "pos": "$pos",
            "temporada":"$temporada"
        }
    },
    {
        "$group": {
            "_id": {"temporada":"$temporada","pos":"$pos"}
        }
    },
    {"$sort":{"_id.temporada":1}},

])





#            podios=Carreras._get_collection().aggregate([
#            { "$match": { "pos":{"$lt":4},"piloto":testPiloto.nombre } },
#            { "$group": {
#                "_id": {"temporada":"$temporada"},
#                "count": { "$sum": 1 }
#            }} 
#        ])


            listaPuntosTemporada=list(puntosTemporada)
            for t in infoPiloto:
                posicion=-1
                #print("***Antes Del Bucle****")
                #print(t.get("_id").get("temporada"))
                #print("************************")
         
                for punto in listaPuntosTemporada:
                    #print(punto.get("_id").get("temporada"))
                    if(punto.get("_id").get("temporada") == t.get("_id").get("temporada")):
                       posicion=punto.get("_id").get("pos")

                #print(t.get("victorias"))
                #print(t.get("podios"))
                #print(t.get("vMedia"))
                #campeonato_t=querysetCampeonato.filter(piloto=p.nombre,temporada=t.get("_id").get("temporada")).only('pos').first()
                p.datosAnuales.append({t.get("_id").get("temporada"):{
                    "categoria":t.get("_id").get("categoria"),
                    "moto":t.get("_id").get("moto"),
                    "num_victorias":t.get("victorias"),
                    "num_podios":t.get("podios"),
                    "posicion_campeonato":posicion,
                    "velMedia":t.get("vMedia"),

                    }})
        

            #for q in queryPiloto:
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
        return pilotos


        

    http_method_names = ['get']

#print(self.request.get_full_path())
class PilotoRedirectViewSet(meviewsets.ModelViewSet):
    """
    list:
    Listado de Pilotos.
    """

    def get_kwargs_for_filtering(self):
        filtering_kwargs = {} 
        my_filter_fields = ('piloto')
        for field in  self.request.query_params: # iterate over the filter fields
            if field.split("__")[0] in my_filter_fields:
                field_value = self.request.query_params.get(field) # get the value of a field from request query parameter
                if field_value: 
                    filtering_kwargs[field] = field_value
        return filtering_kwargs 
    
    serializer_class = PilotoRedirectSerializer
    def get_queryset(self):
        
        pilotos=[]
        filtering_kwargs = self.get_kwargs_for_filtering() # get the fields with values for filtering 
        query=Campeonatos.objects.filter(**filtering_kwargs).distinct('piloto')
        queryset=[]
        for p in query:
            pil=PilotoRedirect()
            pil.nombre=p
            pil.info=self.request.get_full_path().split("/piloto")[0]+"/piloto/info/?piloto="+p
            queryset.append(pil)

        return queryset
    http_method_names = ['get']