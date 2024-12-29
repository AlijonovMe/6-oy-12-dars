from django.contrib import admin
from .models import *


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('id', 'name')
    list_filter = ('id', 'name')
    list_per_page = 10
    search_fields = ('id', 'name')
    actions_on_top = False


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'homework', 'deadline', 'created_at', 'update_at', 'course')
    list_display_links = ('id', 'name')
    list_filter = ('id', 'name')
    list_per_page = 10
    search_fields = ('id', 'name')
    actions_on_top = False


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author', 'lesson', 'created')
    list_display_links = ('id', 'text')
    list_filter = ('id', 'text')
    list_per_page = 10
    search_fields = ('id', 'text')
    readonly_fields = ('author', 'lesson')
    actions_on_top = False


admin.site.register(Course, CourseAdmin)
admin.site.register(Lessons, LessonAdmin)
admin.site.register(Comment, CommentAdmin)
