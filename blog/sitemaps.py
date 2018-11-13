#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/11 16:57
# @Author  : zhaoyan
# @File    : sitemaps.py

from django.contrib.sitemaps import Sitemap
from .models import Post

'''
    不是太明白sitemap的作用是干啥的？后期进一步了解
'''
class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
       return Post.published.all()

    def lastmod(self, obj):
       return obj.publish