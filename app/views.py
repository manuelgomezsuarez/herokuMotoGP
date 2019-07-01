from django.shortcuts import render
from rest_framework_mongoengine import viewsets as meviewsets
from apiMotoGP.serializers import PosicionCarreraSerializer, PosicionCampeonatoSerializer,PosicionDocumentacionSerializer,PilotoSerializer  
from app.models import  Carreras, Campeonatos,Documentacion,Piloto
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

def index(request):
    template = loader.get_template('app/index.html')
    context = {
      
    }
    return HttpResponse(template.render(context,request))

class PosicionCarreraViewSet(meviewsets.ModelViewSet):
    
    serializer_class = PosicionCarreraSerializer
    
    def get_kwargs_for_filtering(self):
        filtering_kwargs = {} 
        my_filter_fields = ('piloto', 'num','temporada','categoria','abreviatura','titulo','lugar','fecha','pos','puntos','pais','equipo','moto','kmh')
        for field in  self.request.query_params: # iterate over the filter fields
            if field.split("__")[0] in my_filter_fields:
                field_value = self.request.query_params.get(field) # get the value of a field from request query parameter
                if field_value: 
                    filtering_kwargs[field] = field_value
        return filtering_kwargs 

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
            print(queryset)
            return arrayQuerySet
        else:
            if filtering_kwargs:
                queryset = Carreras.objects.filter(**filtering_kwargs) # filter the queryset based on 'filtering_kwargs'
                print(queryset)
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
        print(queryset)
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
            print(queryset)
            return arrayQuerySet
        else:
            if filtering_kwargs:
                queryset = Documentacion.objects.filter(**filtering_kwargs) # filter the queryset based on 'filtering_kwargs'
                print(queryset)
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
            urlWikiFoto="Wiki Not Found"

        if filtering_kwargs:
            query=Campeonatos.objects.filter(piloto=filtering_kwargs.get('piloto')).only('piloto','pais','pos').first()
            pilotos=[]
            testPiloto= Piloto()
            testPiloto.nombre=query.piloto
            testPiloto.pais=query.pais
            testPiloto.infoPiloto=infoPiloto
            testPiloto.fotoPiloto=fotoPiloto
            pilotos.append(testPiloto)

            for p in pilotos:
                queryPiloto=Campeonatos.objects.filter(piloto=p.nombre).order_by('temporada').only('pos','temporada','moto','categoria')
                numCampeonatosGanados=Campeonatos.objects.filter(piloto=p.nombre,pos=1).count()
                print(len(queryPiloto))
                p.numCampeonatosGanados=int(numCampeonatosGanados) or 0;
                for q in queryPiloto:
                    vMedia=Carreras.objects.filter(piloto=filtering_kwargs.get('piloto'),temporada=q.temporada).average('kmh')
                    numVictorias=Carreras.objects.filter(piloto=filtering_kwargs.get('piloto'),temporada=q.temporada,pos=1).count()
                    numPodios=Carreras.objects.filter(piloto=filtering_kwargs.get('piloto'),temporada=q.temporada,pos__lt=4).count()

                    p.datosAnuales.append({q.temporada:{
                        "num_victorias":numVictorias,
                        "num_podios":numPodios,
                        "categoria":q.categoria,
                        "velMedia":vMedia,
                        "Moto":q.moto,
                        "Posicion":q.pos}})
        return pilotos


        

    http_method_names = ['get']