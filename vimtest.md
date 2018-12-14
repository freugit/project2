# DJANGO系统
- 环境
- PYTHON3.6
- DJANGO1.8


- 参考资料
- 【django中文教程】(http: // python.usyiyi.cn /)
- django架站的16堂课

# 环境搭建：
- anaconda + pycharm
- anaconda的使用
- conda
list: 显示当前环境安装的包
- conda env
list: 显示安装的虚拟环境列表
- conda
CREATE - N NV_NAME 
PYTHON = 3.6
- ACTIVATE
ENV_NAME(WIN)
- SOURCE
activate
env_name(linux)

- 激活conda的虚拟环境

# 后台需要的流程

# 创建一个第一个django程序
- django - admin
startproject
xxxx

- 启动
- 命令行启动
- cd
xxxx(django工程名称)
- python
manage.py
runserver

- pycharm启动
- 需要配置

# 路由系统 -urls
- 创建app
- app: 负责一个具体业务或者一类具体业务的模块
- python
manage.py
startapp
xxxx
- 路由
- 按照具体的请求url，导入到相应的业务处理模块的一个功能
- django的信息控制中枢
- 本质上是接受的url和相应的处理模块的一个映射
- 在接受url的请求匹配上使用了re
- url的具体格式如urls.py所示

- 需要关注的两点：
- 接受的url是什么，即如何用re对传入url进行匹配
- 已知url匹配到哪个处理模块

- url匹配规则：
- 从上往下一个一个比对
- url格式是分级格式，则按照级别一个一个往下比对，主要对应url包含子url的情况
- 子url一旦被调用，则不会返回到主url
- 'one/two/three'
- 正则以r开头，表示不需要转义，注意( ^)号和美元符号($)
- '/one/two/three/'
配对
r'^one/'
- '/oo/one/two/three/'
不配对r
'^one/'
- '/one/two/three/'
配对
r'three/$'
- '/oo/one/two/three/oo/'
不配对
r'three/$'
- 开头不需要有反斜杠
- 如果从上到下都没有找到合适的匹配内容，则报错
# 2.正常映射
- 把某一个符合re的url映射到事物处理函数中去
- 举例如下：
'''
from showeast import view as sv
urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^normalmap/',sv.normalmap),
]
'''

# 3.带参数的映射
- 在事件处理代码中需要url传入参数，形如： / myurl / param中的param
- 参数都是字符串格式，需要其它格式要自行转换
- 通常的格式如下：
'''
/search/page/432 中的432需要经常变换，所以把它当做参数处理
'''

# 4.url在app中处理
- 如果所有的应用url都集中在主urls.py中，可能导致文件的臃肿
- 可以把urls的具体功能逐渐分散到每个app中
- 从diango.conf.urls导入include
- 注意此时re部分的写法
- 添加include导入
- 使用方法
- 确保include被导入
- 写主路由开头的url
- 写子路由
- 编写views函数
- 同样可以使用参数

# 5.url中的嵌套参数
- 捕获某个参数的某一部分
- 例如url（ / index / page - 3），需要捕获3作为参数
'''
url(r'index_1/(page-(\d+)/)?$',sv.myindex_1) #不太好
url(r'index_2/(?:page-(?p<page_number>\d+)/)?$',sv.myindex_2),#好
'''
- 上述例子会得到两个参数，但?:表明忽略此参数

# 6.传递额外参数
- 参数不仅来自url，还可能是我们自己定义的内容
'''
url(r'extrem/$',sv.extremparam,{name:"liuying"}),

'''
- 附加参数同样适用于include语句，此时对include内所有都添加

# 7.url的反向解析
- 防止硬编码
- 本质上是对每一个url进行命名
- 以后在编码代码中使用url的值，原则上都应该使用反向解析

# views视图
# 1.视图概述
- 视图即视图函数，接受web请求并返回web响应的事物处理函数
- 响应指符合http协议要求的任何内容，包括json，string，html等
- 本章忽略事物处理，重点在如何返回结果上

# 2.其它简单视图
- django.http给我们提供了很多和httpresponse类似的简单视图
，通过查看django.http我们可以知道
- 此类视图使用方法基本类似，可以通过return语句直接反馈给浏览器
- http404为exception子类，所以需要raise使用

# 3.httpresponse详解
- 方法
- init: 使用页内容实例化httpresponse对象
- write(content): 以文件的方式写
- flush(): 以文件的方式输出缓冲区
- set_cookie(key, value='', max_age=none, expires=none): 设置cookie
- key, value都是字符串类型
- max_age是一个整数，表示在指定秒数后过期
- expires是一个datetime或timedelta对象，会话将在这个指定的日期 / 时间过期
- max_age和expires二选一
- 如果不指定过期时间，则两个星期后过期
- delete_cookie(key): 删除指定的key的cookie，如果不存在则什么都不会发生

# 4.httpresponseredirect(重定向)
- 重定向页面
- 导入后使用，第一个参数为重定向后网址

# 5.request对象
- request介绍
- 服务器接收到http协议的请求后，会根据报文内容创建httprequest对象
- 视图函数的第一个参数是httprequest对象
- 在django.http模块中定义了httprequest对象的api
- 属性
- 下面除非特别说明，属性都是只读的
- path: 一个字符串，表明请求的页面的完整路径，不包含域名
- method: 一个字符串，表明请求使用的http方法，常用值包括：get, post
- encoding: 一个字符串，表明提交的数据的编码方式：
- 如果为none则表示使用浏览器的默认设置，一般为utf - 8
- 这个属性时是可写的，可以通过修改它来修改访问表单数据使用编码
- get: 一个类似于字典的对象，包括get请求方式的所有参数
- post: 一个类似于字典的对象，包括post请求方式的所有参数
- files: 一个类似于字典的对象，包括所有的上传文件
- cookies: 一个标准的python字典，包含所有的cookie，键和值都为字符串
- session: 一个即可读又可写的类似于字典的对象，表示当前会话，只有当django启用会话的支持的时候才可用，详细见状态保持

- 方法
- is_ajax(): 如果请求是通过xmlhttprequest发起的，则返回true

- querydict对象
- 定义在DJANGO.HTTP.QUERYDICT
- REQUEST对象的属性GET, POST都是QUERYDICT类型的对象
- 与PYTHON字典不同，QUERYDICT用来处理同一个键带有多个值的情况
- 方法GET(): 根据键获取值
- 只能获取键的一个值
- 如果一个键同时拥有多个值，获取最后一个值
- 方法GETLIST(): 根据键获取值
- 将键的值以列表的形式返回，可以获取一个键的多个值

- GET属性
- QUERYDICT类型的对象
- 包括GET请求方式的所有参数
- 与URL请求地址的参数对应，位于？后面
- 参数的格式是键值对，如KEY = VALUE
- 多个参数之间，使用 & 连接，例如KEY1 = VALUE1 & KEY2 = VALUE2

- POST
- 提交表单数据，由于安全原因，需要禁用SETTINGS的MIDDLEWARE中的CRS安全组件
- 。。。
43
- 手动编写视图
- 实验目的
- 利用DJANGO快捷函数手动编写视图处理函数


- 编写过程中理解视图运行的原理
- 分析
- DJANGO把所有请求信息封装如REQUEST
- DJANGO通过URLS模块把相应请求跟事件处理函数链接起来，并把REQUEST作为参数传入
- 在相应的处理函数中，我们需要完成两部分
- 处理业务
- 把结果封装返回，我们可以使用简单的HTTPRESPONSE, 同样也可以手动封装
- 本案例不介绍业务处理，把目光集中在如何渲染结果并返回

- RENDER(()REQUEST, TEMPLATE_NAME[, CONTEXT][, CONTENT_INSTANCE])
- 使用模板和一个给定的上下文环境，返回一个渲染的HTTPRESPONSE
- request: django的传入请求
- template_name: 模板名称
- content_instance: 上下文环境
- render
- render
- render
- render
- render
- render
- render
- render
- render
- render
- 根据给定的上下文字典渲染给定模板，返回渲染后的HTTPRESPONSE

- 根据给定的上下文字典渲染给定模板，返回渲染后的HTTPRESPONSE
- 系统内建视图
- 可以直接使用
- 使用
