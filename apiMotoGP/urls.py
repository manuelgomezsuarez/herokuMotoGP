from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import permissions




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('app.urls')),

]