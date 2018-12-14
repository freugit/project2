from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
import json

def one(request):
    return render(request,'helloworld1.html')
# Create your views here.

def two(request):
    #用来存放向模板中存放的数据
    ct = dict()
    ct['name'] = "王晓静"
    ct['name2'] = "李晓静"
    ct['name3'] = "张晓静"
    return render(request,'two.html',context=ct)
def three(request):
    ct = dict()
    ct['score'] = [99,87,96,95,94]
    return render(request,'three.html',context=ct)
def four(request):
    ct = dict()
    ct["name"] = "张晓静"
    return render(request,'four.html',context=ct)
def five_get(request):
    return render(request,'five.html')
def five_post(request):
    print(request.POST)
    return render(request,'two.html')

def jsonrsp(reuqest):
    res = Person.objects.all()
    resj = list()
    for resd in res:
        resj.append(model_to_dict(resd))
    jr = JsonResponse({"data":resj})
    return jr
@csrf_exempt
def submit(request):
    print(request.POST)
    print(request.body)
    if request.method=='POST':
        jsonres = json.loads(request.body)
        print(jsonres['name'],jsonres['date'],jsonres['content'])
        Person.objects.create(name=jsonres['name'],date=jsonres['date'],content=jsonres['content'])

    return HttpResponse('OK')



