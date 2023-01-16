# --*--:coding utf-8 --*--
# @Time: 2023-01-16 22:13
# @Author: 李月初
# @FIle: forms
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'id': 'name',
        'class': 'contact_input',
        'required': 'required',
        'placeholder': '姓名',
        'tabindex': '1',
    }))
    email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={
        'id': 'email',
        'class': 'contact_input',
        'required': 'required',
        'placeholder': '邮箱',
        'tabindex': '2',
    }))
    topic = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'id': 'topic',
        'class': 'contact_input',
        'required': 'required',
        'placeholder': '主题',
        'tabindex': '3',
    }))
    text = forms.CharField(widget=forms.Textarea(attrs={
        'id': 'text',
        'class': 'contact_area',
        'required': 'required',
        'placeholder': '信息',
        'tabindex': '4',
        'rows': 7,
    }))

    class Meta:
        model = Contact
        fields = ['name', 'email', 'topic', 'text']