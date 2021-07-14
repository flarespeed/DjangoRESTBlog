from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from blog.models import Thread, Comment
from rest_framework import viewsets
from rest_framework import permissions
from blog.serializers import ThreadSerializer, CommentSerializer, UserSerializer
from blog.permissions import AdminOrReadOnly

class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = [AdminOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AdminOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [AdminOrReadOnly]