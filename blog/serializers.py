from django.contrib.auth.models import User
from blog.models import Thread, Comment
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

class NonRecursiveCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['url', 'user', 'time', 'content']

class ThreadSerializer(serializers.HyperlinkedModelSerializer):
    comments = NonRecursiveCommentSerializer(many=True, read_only=True)
    class Meta:
        model = Thread
        fields = ['url', 'user', 'time', 'content', 'title', 'comments']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['url', 'thread', 'user', 'time', 'content']