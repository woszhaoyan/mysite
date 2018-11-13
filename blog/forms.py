#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/6 21:21
# @Author  : zhaoyan
# @File    : forms.py

from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields = ('name', 'email', 'body')