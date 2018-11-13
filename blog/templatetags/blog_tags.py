#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/11 11:13
# @Author  : zhaoyan
# @File    : blog_tags.py

from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

'''
    该模块展示了自定义tag的功能：
        1. simple_tag 处理数据并返回一个字符串(string)
        2. inclusion_tag ： 处理数据并返回一个渲染过的模板(template)
        3. assignment_tag : 处理数据并在上下文(context)中设置一个变量(variable)
'''

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_post(count):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts' : latest_posts}

@register.assignment_tag
def get_most_comment_posts(count=5):
    # annotate这个函数是干嘛的,学习文档:https://www.cnblogs.com/wumingxiaoyao/p/7065471.html
    # Count 计算每个post下的评论数，其接受的参数为需要计数的模型的名称（comments）
    return Post.published.annotate(total_comments=Count('comments')).order_by("-total_comments")[:count]



'''
    下面为自定义过滤器
'''

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))