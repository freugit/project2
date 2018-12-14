# Django系统
- 环境
    - python3.6
    - django1.8

- 参考资料
    - 【Django中文教程】(http://python.usyiyi.cn/)
    - django架站的16堂课

# 环境搭建：
- anaconda+pycharm
- anaconda的使用
    - conda list:显示当前环境安装的包
    - conda env list:显示安装的虚拟环境列表
    - conda create -n env_name python=3.6
    - 激活conda的虚拟环境
        - activate env_name(win)
        - source activate env_name(linux)
        
# 后台需要的流程

# 创建一个第一个django程序
- django-admin startproject xxxx

- 启动
    - 命令行启动
        - cd xxxx(django工程名称)
        - python manage.py runserver
        
    - pycharm启动
        - 需要配置
        
# 路由系统 -urls
- 创建app
    - app:负责一个具体业务或者一类具体业务的模块
    - python manage.py startapp xxxx
- 路由
    - 按照具体的请求url，导入到相应的业务处理模块的一个功能
    - django的信息控制中枢
    - 本质上是接受的url和相应的处理模块的一个映射
    - 在接受url的请求匹配上使用了RE
    - URL的具体格式如urls.py所示

- 需要关注的两点：
    - 接受的URL是什么，即如何用RE对传入URL进行匹配
    - 已知URL匹配到哪个处理模块
    
- URL匹配规则：
    - 从上往下一个一个比对
    - url格式是分级格式，则按照级别一个一个往下比对，主要对应url包含子url的情况
    - 子url一旦被调用，则不会返回到主url
        - 'one/two/three'
    - 正则以r开头，表示不需要转义，注意(^)号和美元符号($)
        - '/one/two/three/' 配对 r'^one/'
        - '/oo/one/two/three/' 不配对r'^one/'
        - '/one/two/three/' 配对 r'three/$'
        - '/oo/one/two/three/oo/' 不配对 r'three/$'
        - 开头不需要有反斜杠
        - 如果从上到下都没有找到合适的匹配内容，则报错
# 2.正常映射
- 把某一个符合RE的URL映射到事物处理函数中去
    - 举例如下：
        '''
        from showeast import view as sv
        urlpatterns = [
            url(r'^admin/',admin.site.urls),
            url(r'^normalmap/',sv.normalmap),
        ]
        '''       

    
# 3.带参数的映射
- 在事件处理代码中需要URL传入参数，形如：/myurl/param中的param
- 参数都是字符串格式，需要其它格式要自行转换
- 通常的格式如下：
    '''
    /search/page/432 中的432需要经常变换，所以把它当做参数处理
    '''

# 4.url在APP中处理
- 如果所有的应用URL都集中在主urls.py中，可能导致文件的臃肿
- 可以把urls的具体功能逐渐分散到每个app中
    - 从diango.conf.urls导入include
    - 注意此时RE部分的写法
    - 添加include导入
- 使用方法
    - 确保include被导入
    - 写主路由开头的url
    - 写子路由
    - 编写views函数
- 同样可以使用参数

# 5.URL中的嵌套参数
- 捕获某个参数的某一部分
- 例如URL（/index/page-3），需要捕获3作为参数
    '''
    url(r'index_1/(page-(\d+)/)?$',sv.myindex_1) #不太好
    url(r'index_2/(?:page-(?P<page_number>\d+)/)?$',sv.myindex_2),#好
    '''
- 上述例子会得到两个参数，但?:表明忽略此参数

# 6.传递额外参数
- 参数不仅来自URL，还可能是我们自己定义的内容
    '''
    url(r'extrem/$',sv.extremParam,{name:"liuying"}),
    
    '''
- 附加参数同样适用于include语句，此时对include内所有都添加    
 
# 7.URL的反向解析
- 防止硬编码
- 本质上是对每一个URL进行命名
- 以后在编码代码中使用URL的值，原则上都应该使用反向解析

# views视图
# 1.视图概述
- 视图即视图函数，接受web请求并返回web响应的事物处理函数
- 响应指符合HTTP协议要求的任何内容，包括json，string，html等
- 本章忽略事物处理，重点在如何返回结果上

# 2.其它简单视图
- django.http给我们提供了很多和HttpResponse类似的简单视图
，通过查看django.http我们可以知道
- 此类视图使用方法基本类似，可以通过return语句直接反馈给浏览器
- Http404为Exception子类，所以需要raise使用


# 3.HttPResponse详解
- 方法
    - init:使用页内容实例化HttPResponse对象
    - write(content):以文件的方式写
    - flush():以文件的方式输出缓冲区
    - set_cookie(key,value='',max_age=None,expires=None):设置cookie
        - key,value都是字符串类型
        - max_age是一个整数，表示在指定秒数后过期
        - expires是一个datetime或timedelta对象，会话将在这个指定的日期/时间过期
        - max_age和expires二选一
        - 如果不指定过期时间，则两个星期后过期
    - delete_cookie(key):删除指定的key的Cookie，如果不存在则什么都不会发生
    
# 4.HttpResponseRedirect(重定向)
- 重定向页面
- 导入后使用，第一个参数为重定向后网址

# 5.Request对象
- Request介绍
    - 服务器接收到Http协议的请求后，会根据报文内容创建HttpRequest对象
    - 视图函数的第一个参数是HttpRequest对象
    - 在django.http模块中定义了HttPRequest对象的API
- 属性
    - 下面除非特别说明，属性都是只读的
    - path:一个字符串，表明请求的页面的完整路径，不包含域名
    - method:一个字符串，表明请求使用的HTTP方法，常用值包括：GET,POST
    - encoding:一个字符串，表明提交的数据的编码方式：
        - 如果为None则表示使用浏览器的默认设置，一般为utf-8
        - 这个属性时是可写的，可以通过修改它来修改访问表单数据使用编码
    - GET:一个类似于字典的对象，包括get请求方式的所有参数
    - POST:一个类似于字典的对象，包括POST请求方式的所有参数
    - FILES:一个类似于字典的对象，包括所有的上传文件
    - COOKIES:一个标准的Python字典，包含所有的cookie，键和值都为字符串
    - session:一个即可读又可写的类似于字典的对象，表示当前会话，只有当django启用会话的支持的时候才可用，详细见状态保持

- 方法
    - is_ajax():如果请求是通过XMLHttpRequest发起的，则返回True

- QueryDict对象
    - 定义在django.http.QueryDict
    - request对象的属性GET,POST都是QueryDict类型的对象
    - 与Python字典不同，QueryDict用来处理同一个键带有多个值的情况
    - 方法get():根据键获取值
        - 只能获取键的一个值
        - 如果一个键同时拥有多个值，获取最后一个值
    - 方法getlist():根据键获取值
        - 将键的值以列表的形式返回，可以获取一个键的多个值
    
- GET属性
    - QueryDict类型的对象
    - 包括get请求方式的所有参数
    - 与url请求地址的参数对应，位于？后面
    - 参数的格式是键值对，如key=value
    - 多个参数之间，使用&连接，例如key1=value1&key2=value2

- POST
    - 提交表单数据，由于安全原因，需要禁用settings的Middleware中的crsf安全组件
    - 。。。
    
- 手动编写视图
    - 实验目的
    - 利用django快捷函数手动编写视图处理函数
    - 编写过程中理解视图运行的原理
    
- 分析
    - django把所有请求信息封装如request
    - django通过urls模块把相应请求跟事件处理函数链接起来，并把request作为参数传入
    - 在相应的处理函数中，我们需要完成两部分
        - 处理业务
        - 把结果封装返回，我们可以使用简单的HttpResponse,同样也可以手动封装
        - 本案例不介绍业务处理，把目光集中在如何渲染结果并返回
        
    - render(request,template_name[,context][,content_instance])
    - 使用模板和一个给定的上下文环境，返回一个渲染的HttPResponse
    - request:django的传入请求
    - template_name:模板名称
    - content_instance:上下文环境
    - render_to_response
        - 根据给定的上下文字典渲染给定模板，返回渲染后的HttpResponse
        
- 系统内建视图
    - 可以直接使用
    - 使用 from django.views import defaults，可以使用各种内建视图，如page_not_found,等等

- 装饰类
    - 类的方法和独立方法不同，不能直接应用装饰器，需要用method_decorator装饰
        '''
        from django.contrib.auth.decorators import login_required
        from django.utils.decorators import method_decorator
        from django.views.generic import TemplateView
        
        class ProtectedView(TemplateView):
            template_name = 'secret.html'
            
            @method_decorator(login_required)
            def dispatch(self,*args,**kwargs):
                return super(ProtectedView,self).dispatch(*args,**kwargs)
        '''

# Models 模型
- ORM
    - ObjectRelationMap:把面向对象转换成关系型数据库思想，操作上把类对应表格
    - 类对应表格
    - 类中的属性对应表中的字段
    - 在应用中的models.py文件中定义class
    - 所有需要使用ORM的class都必须是models.Model的子类
    - class中的所有属性对应表格中的字段
    - 字段的类型都必须使用models.xxx不能使用python的类型
    - 在django中，Models负责跟数据库交互
- django链接数据库
    - 自带默认数据库Sqlite3
        - 关系型数据库
        - 轻量级
    - 建议开发时使用sqlite3，部署用mysql之类数据库
    - 切换数据库在settings中设置。  
            #django链接mysql
            DATABASES = {
                'default' = {
                    'ENGINE':'django.db.backends.mysql',
                    'NAME':'数据库名',
                    'PASSWORD':'数据库密码',
                    'HOST':'127.0.0.1',
                    'PORT':'3306',
                }
            }
            
    - 需要在项目文件下的__init__文件导入pymysql包  
        import pymysql
        pymysql.install_as_MySQLdb()
        
# models类的使用
- 定义和数据库表映射的类
    - 在应用中的models.py文件中定义class
    - 所有需要使用ORM的class都必须是models.Model的子类
    - class中的所有属性对应表格中的字段
    - 字段的类型都必须使用models.xxx，不能使用python中的类型

- 字段常用参数
    1.max_length:规定数值的最大长度
    2.blank:是否允许字段为空，默认不允许
    3.null:在DB中是否允许为null,默认为false
    4.default:默认值
    5.unique:是否唯一
    6.verbose_name:假名
    
- 数据库的迁移
    1. 在命令行中，生成数据迁移的语句（生成sql语句）
        '''
        python manage.py makemigrations
        '''
    2. 在命令行中，输入数据迁移的指令
        '''
        python manage.py migrate            
        '''
        ps:如果迁移中出现没有变化或者报错，可以尝试强制迁移
#.  强制迁移命令
- python3 manage.py makemigrations 应用名             
- python3 manage.py migrate 应用名

3.对于默认数据库，为了避免混乱，如果数据库中没有数据，每次迁移前要把
自带的sqlite3数据库删除

### 1.查看数据库中的数据
'''
1.启动命令行:python manage.py shell
ps:注意点:对ORM的操作分为静态函数和非静态函数两种，静态指在内存中只有一份数据
2. 在命令行中导入相应的映射类：
    from 应用名.models import 类名
3.使用objects属性操作数据库，objects是模型中实际与数据库交互的实体
4.查询命令
    - 类名.objects.all()查询数据库表中的所有内容，返回的结果是一个QuerySet
    - 类名.objects.filter(条件)
'''
### 2.添加数据
  - s = Student() //实例化对象
    //给对象的属性赋值
    s.name = "张三"
    s.age = 18
    s.address = "云南"
    s.phone = '13222331112'
    //保存到数据库
    s.save()
### 常用的查找方法
1.通用查找格式：属性名 __（下面内容） = 值
- gt:大于
- gte:大于等于
- lt:小于
- lte:小于等于
- range:范围
- year:年份
- isnull:是否为空
2.查找等于指定值的格式，属性名 = 值
3.模糊查找:属性名 __（下面内容） = 值
- exact:精确等于
- iexact:不区分大小写
- contains:包含
- startwith:以。。开头
- endwith:以。。结尾

# 数据库表的关系
- 多表联查:利用多个表联合查找某一项或多项信息
- 1.OneToOne:
    - 建立关系，在模型任一边即可，使用OneToOneField定义
    - add:
        - 添加没有关系的一边，直接实例化保存就可以
            -  >>> s = School()
               >>> s.school_id = 2
               >> s.school_name = "幽灵学院"
               >> s.save()
  
        - 添加有关系的一边，使用create方法或者直接实例化
            -  >>> m = Manager()
               >>> m.manage_id = 10
               >>> m.manage_name = "大拿"
               >>> m.my_school = s
               >>> m.save()
            -  或者
               >>> m = Manager.objects.create(manage_id = 20,manage_name = "二拿",my_school = ss[0])
    - query:
        - 由子表查母表
            >>> Manager.objects.get(manage_name="大拿").my_school.school_name
        - 由母表查子表
            >>> s = School.objects.get(manager__manage_name="大拿")
    - change:
        - 单个修改用save()
        - 批量修改用update()
        - 无论对子表还是对母表的修改
        
    - delete:直接使用delete删除
- 2.OneToMany:
    - 一个表格的一个数据项/对象等，可以有很多另一个表格的数据项
    - 比如:一个学校可以有很多老师，但一个老师只能在一个学校上班
    - 使用:
        - 使用ForeignKey
        - 在多的一边，上面的例子里是Teacher表里边使用ForeignKey定义
        
    - Add
        - 与一对一情况类似，使用create或者new定义    
        - create把属性都填满
        - new一项一项的填，然后save()
    - Query
        - 以学校和老师的例子为准
        - 如果知道老师，查学校，则通过增加的关系属性，直接使用
        - 例如，查t1老师是哪个学校的，直接通过my_school属性查找
        - 反查，有学校，我想知道这个学校的所有老师，则系统已经自动在学校下增加了一个（小写）teacher_set属性，来存放所有Teacher关系，用teacher_set.all()返回所有teacher对象    
- 3.ManyToMany:
    - 表示任意一个表的数据都可以拥有对方表格的多项数据，反之亦然
    - 比如典型的例子就是学生和老师的关系
    - 使用上，在任意一方，使用ManyToMany定义，只需要定义一边
    - Add:
        - 添加老师，则在student.teachers.add(),注意应该先save()在添加
        
    - Query
        - 跟一对多类似，使用_set查询，即teacher.student_set.all()
        

# 模板系统
- 模板:一组相同或者相似的页面，在需要个性化的地方留白，需要的时候只是用数据填充就可以使用
- 步骤:
    1.在settings进行设置，TEMPLATES下的DIR增加模板所在目录
    2.在templates文件夹下编写并调用

## 模板-变量
- 变量的表示方法：{{var_name}} 
- 在系统调用模板的时候，会用相应的数据查找相应的变量名称，如果能找到，就填充进去，不能找到，就留空  
- 案例two.html
## 模板-标签
- for 标签：{% for .. in .. %}
- 用法：
    {% for .. in .. %}
    #循环语句
    {% endfor %}
- 案例 three

- if 标签
- 用法
    {% if 条件 %}
        条件成立时执行语句
    {% elif 条件 %}
        条件成立时执行语句
    {% else %}
        以上条件都不成立时执行语句
    {% endif %}
- 案例 four

## csrf标签
- csrf：跨站请求伪造
- 在提交表单的时候，表单页面需要加上{% crsf_token %}
- 案例five_get,five_post

# session
- 为了应对HTTP的无状态性
- 用来保存用户比较敏感的信息
- 属于request的一个属性
- 常用操作：
    - request.session.get(key,defaultValue)
    - request.session.clear():清除全部
    - request.session[key] = value:赋值
    - request.session.flush():删除当前会话并清除会话的session+
    - del request.session[key]:删除值

# 分页
- django提供现成的分页器用来对结果进行分页
- 代码： 
        from django.core.paginator import Paginator
        ...
        stu = Students.objects.all()
        #两个参数，第一个是数据来源，也即是从数据库中查询出的结果
        第二个是单页返回数据量
        p = Paginator(stu,40)
        #对Paginator进行配置或者对变量属性使用
        print(p.count)# p里面有多少数据
        print(p.num_pages) #页面总数
        print(p.page_range)#页码列表，从1开始
        #取得第3页的内容
        #如果页码不存在，报异常InvalidPage
        return p.page(3)
      
# Ajax
xxx

# 基于类的视图
- 可以针对http协议不同的方法创建不同的函数
- 可以使用Mixin等oop技术
- Mixin
    - 把来自父类的行为和属性组合在一起
    - 解决多重继承的问题
- 代码示例 session_example中的views.py

# admin
- 打开urls.py
- 创建超级用户 python manage.py createsuperuser
- 配置settings文件

## 绑定管理模型
- 在app的admin.py中注册
## 设置admin管理类
- 实现方式
    - admin.ModelAdmin
    - 装饰器
    
- 修改页面显示数量:list_per_page
- 操作选项：actions_on_top/button
- 控制列表中显示的内容:list_display=[]
- 将方法作为列显示
    - 函数必须有返回值
    - 设置short_description作为显示内容
    - 排序使用admin_order_field
    
- 关联对象
    - 使用方法
    
        

    
    

