from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse

'''
视图函数需要一个参数，类型应该是HttpRequest

'''


def do_normalmap(request):
    return HttpResponse("This is normalmap")

def with_param(request,year,month):
    return HttpResponse("This is with_param:{0},{1}".format(year,month))


def do_app(r):
    return HttpResponse("here is response for liudana")

def do_param2(r,pn):
    return HttpResponse('Page Number is {0}'.format(pn))

def do_extreamParam(r,name):
    return HttpResponse("my name is {0}".format(name))

def revParse(r):
    return HttpResponse("you requested URL is {0}".format(reverse('askname')))

def v2_exp_view(r):
    raise Http404
    return HttpResponse("OK")

def v10_view(r):
    return HttpResponseRedirect(reverse('v11'))

def v11_view(r):
    return HttpResponse('这是v11的返回结果')

def v8_get(request):
    rst = ''
    for k,v in request.GET.items():
        rst += k + '-->'+v
        rst += '，'

    return HttpResponse('Get value of Request is {0}'.format(rst))


def render_test(request):
    # 环境变量
    # c = dict()
    rsp = render(request,'render.html')
    return  rsp

def render2_test(request):
    # 环境变量
    c = dict()
    c['name'] = 'LiuDaNa'
    rsp = render(request,'render2.html',context=c)
    return rsp

from django.views import defaults

def render3_test(reuqest):
    return defaults.bad_request()

