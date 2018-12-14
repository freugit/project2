from django.conf.urls import include,url
from django.contrib import admin
from . import views as tv

urlpatterns = [

    url(r'^liudana/',tv.do_app )


]