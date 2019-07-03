from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters
from app.views import PosicionCarreraViewSet,PosicionCampeonatoViewSet,PosicionDocumentacionViewSet,index,PilotoViewSet,PilotoRedirectViewSet
from django.urls import path

merouter = merouters.DefaultRouter()
merouter.register(r'carrera', PosicionCarreraViewSet,base_name="carrera")
merouter.register(r'campeonato', PosicionCampeonatoViewSet,base_name="campeonato")
merouter.register(r'documentacion', PosicionDocumentacionViewSet,base_name="documentacion")
merouter.register(r'piloto', PilotoRedirectViewSet,base_name="piloto")
merouter.register(r'piloto/info', PilotoViewSet,base_name="pilotoInfo")



urlpatterns = [
    path('', index, name='index'),

]
urls2=[]
for r in merouter.urls:
    if not "id" in str(r):
        urls2.append(r)

urlpatterns+=urls2