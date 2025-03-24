from rest_framework import serializers
from .models import User, AIProfile, Chat, VoiceClone

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AIProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIProfile
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

class VoiceCloneSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceClone
        fields = '__all__'
