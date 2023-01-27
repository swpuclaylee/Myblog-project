# --*--coding: utf-8 --*--
# @Time: 2023-01-27 16:34
# @Author: 李月初
# @FIle: serializers
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "name",
            "email",
            "url",
            "text",
            "created_time",
            "post",
        ]
        read_only_fields = [
            "created_time",
        ]
        extra_kwargs = {"post": {"write_only": True}}