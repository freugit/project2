"""django_tpl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mytpl import views as v

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^one/',v.one),
    #url(r'^index.js',v.rtjs),
    #url(r'^vue.min.js',v.rtvjs),
    url(r'^two/',v.two),
    url(r"^three/",v.three),
    url(r"^four/",v.four),
    url(r"^five/",v.five_get),
    url(r'^five_post/',v.five_post),
    url(r'^json.jsp/',v.jsonrsp),
    url(r'^submit/',v.submit),
    url(r'^index/',v.index)
]
