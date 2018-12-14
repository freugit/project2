from django.contrib import admin
from sess.models import Student,ClassRoom,Teacher

# Register your models here.

#admin.site.register(Student)
#admin.site.register(ClassRoom)
#admin.site.register(Teacher)
@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    pass

class TeacherAdmin(admin.ModelAdmin):
    list_per_page = 2
    actions_on_bottom = True
    actions_on_top = False
    list_display = ['name','room','curTime','getRoomName']
    search_fields = ['name']
    fieldsets = (
        ('基本信息',{'fields':['name']}),
        ('详细信息',{'fields':['name','course','room']})
    )

class StudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)


admin.site.site_header = '这是站点头部'
admin.site.site_title = '这是站点标题'
admin.site.index_title = '这是首页标题'
#admin.site.register(ClassRoom,ClassRoomAdmin)