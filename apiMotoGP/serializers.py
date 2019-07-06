from rest_framework_mongoengine import serializers
from app.models import Carreras, Campeonatos, Documentacion, Piloto, PilotoRedirect,Dashboard
 

    
class PosicionCarreraSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Carreras
        exclude=['id',]

class PosicionCampeonatoSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Campeonatos
        exclude=['id',]
class PosicionDocumentacionSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Documentacion
        exclude=['id',]

class PilotoSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Piloto
        exclude=['id',]

class PilotoRedirectSerializer(serializers.DocumentSerializer):
    class Meta:
        model = PilotoRedirect
        exclude=['id',]

class DashboardSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Dashboard
        exclude=['id',]