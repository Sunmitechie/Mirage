from django.shortcuts import render
from rest_framework import generics
from .models import User, AIProfile, Chat, VoiceClone
from .serializers import UserSerializer, AIProfileSerializer, ChatSerializer, VoiceCloneSerializer

# User API
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# AI Profile API
class AIProfileListCreate(generics.ListCreateAPIView):
    queryset = AIProfile.objects.all()
    serializer_class = AIProfileSerializer

class AIProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AIProfile.objects.all()
    serializer_class = AIProfileSerializer

# Chat API
class ChatListCreate(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

# Voice Clone API
class VoiceCloneListCreate(generics.ListCreateAPIView):
    queryset = VoiceClone.objects.all()
    serializer_class = VoiceCloneSerializer

class VoiceCloneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VoiceClone.objects.all()
    serializer_class = VoiceCloneSerializer

