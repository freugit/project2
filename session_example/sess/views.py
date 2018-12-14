from django.shortcuts import render
from django.views.generic import ListView
from .models import *
def mySess(request):
    print(type(request.session))
    print(request.session)
    #返回session中teacher_name的值，如果没有则返回默认值NoName
    print(request.session.get('name','NoName'))
    #清空session里所有的值
    request.session.clear()
    request.session['name']="王晓静"
    print('In my Sess')
    print(request.session.get('name',"NoName"))
    ct = dict()
    ct['name'] = request.session.get('name',"NoName")
    print('Done')
    return render(request,'two.html',context=ct)
# Create your views here.

'''
#基于类的视图
class StudentListView(ListView):
''' '''   需要设置两个主要内容
    1.queryset:数据来源集合
    2.template_name:模板名称
    '''
'''
    queryset = Student.objects.all().filter(gender='男')
    template_name = "student.list.html"
'''