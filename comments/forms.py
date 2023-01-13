# --*--coding: utf-8 --*--
# @Time: 2023-01-14 1:54
# @Author: 李月初
# @FIle: forms

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']