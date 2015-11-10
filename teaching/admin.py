from django.contrib import admin
from models import Teacher,Student

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','experience')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone')

admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student,StudentAdmin)

