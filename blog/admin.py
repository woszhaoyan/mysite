# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Post, Comment
from django.contrib import admin

from django.contrib import admin

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    #设置展示的字段 list_display
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    #设置过滤的字段，在管理端的右侧
    list_filter = ('status', 'created', 'publish', 'author')
    # 搜索栏，是针对设置的字段进行搜索，本例为title和body
    search_fields = ('title', 'body')
    #自动填充，用title字段
    prepopulated_fields = {'slug': ('title',)}
    # 在添加post时，作者的检索，使用作者的id，而不是名字
    raw_id_fields = ('author',)
    #设置检索的导航栏--快速检索
    date_hierarchy = 'publish'
    #指定排序的字段
    ordering = ['status', 'publish']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
