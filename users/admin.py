from django.contrib import admin

from users.models import User


@admin.action(description='Присвоить значение "Преподаватель"')
def make_teacher(modeladmin, request, queryset):
    queryset.update(is_teacher=True)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'fullname', 'qualification', 'is_teacher')
    search_fields = ('pk', 'email', 'fullname', 'qualification', 'is_teacher')
    actions = [make_teacher]
