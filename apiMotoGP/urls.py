from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import permissions
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='MotoGP API')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('app.urls')),
    url(r'^api/', schema_view),

]