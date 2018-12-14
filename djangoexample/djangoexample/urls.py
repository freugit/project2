"""djangoexample URL Configuration

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
from django.conf.urls import include,url
from django.contrib import admin
from teacher import views as tv
from teacher import teacher_url

'''
比如约定由teacher处理的路由以teacher开头
'''
urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^normalmap/',tv.do_normalmap),
    url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])',tv.with_param),
    url(r'^teacher/',include(teacher_url)),
    url(r'^book/(?:page-(?P<pn>\d+)/)$',tv.do_param2),
    url(r'^youname/$',tv.do_extreamParam,{'name':'liudana'}),
    url(r'^yourname/$',tv.revParse,name="askname"),
    url(r'^v2_exp',tv.v2_exp_view),
    url(r'^v10/$',tv.v10_view),
    url(r'^v11_hello/$',tv.v11_view,name='v11'),
    url(r'^v8',tv.v8_get),
    url(r'^render_test',tv.render_test),
    url(r'^render2_test',tv.render2_test),
    url(r'^reder3_test',tv.render3_test)
]
