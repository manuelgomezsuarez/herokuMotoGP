from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls

from rest_framework import permissions




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('app.urls')),
    url(r'^docs/', schema_view),

]