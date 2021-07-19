from django.contrib.auth.models import User
from blog.models import Thread, Comment
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}, 'email': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class NonRecursiveCommentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = ['url', 'user', 'time', 'content']
        extra_kwargs = {'user': {'read_only': True},'url': {'read_only': True}}

class ThreadSerializer(serializers.HyperlinkedModelSerializer):
    comments = NonRecursiveCommentSerializer(many=True, read_only=True)
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Thread
        fields = ['url', 'user', 'time', 'content', 'title', 'comments']
        extra_kwargs = {'user': {'read_only': True},'url': {'read_only': True}}

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = ['url', 'thread', 'user', 'time', 'content']
        extra_kwargs = {'user': {'read_only': True},'url': {'read_only': True}}