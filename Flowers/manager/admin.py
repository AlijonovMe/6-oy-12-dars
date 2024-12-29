from django.contrib import admin
from .models import *


class TypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('id', 'name')
    list_filter = ('id', 'name')
    list_per_page = 10
    search_fields = ('id', 'name')
    actions_on_top = False


class FlowersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'count', 'published', 'type')
    list_display_links = ('id', 'name')
    list_filter = ('id', 'name')
    list_editable = ('price', 'count', 'published', 'type')
    list_per_page = 10
    search_fields = ('id', 'name')
    actions_on_top = False


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author', 'flower', 'created')
    list_display_links = ('id', 'text')
    list_filter = ('id', 'text')
    list_per_page = 10
    search_fields = ('id', 'text')
    readonly_fields = ('author', 'flower')
    actions_on_top = False


admin.site.register(Types, TypesAdmin)
admin.site.register(Flowers, FlowersAdmin)
admin.site.register(Comment, CommentAdmin)
