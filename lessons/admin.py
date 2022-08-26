from django.contrib import admin

# Register your models here.
from lessons.models import Class, Subject, LearningActivity


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    search_fields = ('pk',  'name',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    search_fields = ('pk',  'name',)

@admin.register(LearningActivity)
class LearningActivityAdmin(admin.ModelAdmin):
    list_display = ('pk', 'teachers', 'rooms', 'subjects')
    search_fields = ('pk', 'teachers', 'rooms', 'subjects')

