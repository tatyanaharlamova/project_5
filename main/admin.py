from django.contrib import admin
from main.models import Students, Subject


# Register your models here.
#admin.site.register(Students)


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'student',)
    list_filter = ('student',)
