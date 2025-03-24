from django.urls import path
from .views import UserListCreate, UserDetail, AIProfileListCreate, AIProfileDetail, ChatListCreate, ChatDetail, VoiceCloneListCreate, VoiceCloneDetail

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),

    path('ai-profiles/', AIProfileListCreate.as_view(), name='ai-profile-list'),
    path('ai-profiles/<int:pk>/', AIProfileDetail.as_view(), name='ai-profile-detail'),

    path('chats/', ChatListCreate.as_view(), name='chat-list'),
    path('chats/<int:pk>/', ChatDetail.as_view(), name='chat-detail'),

    path('voice-clones/', VoiceCloneListCreate.as_view(), name='voice-clone-list'),
    path('voice-clones/<int:pk>/', VoiceCloneDetail.as_view(), name='voice-clone-detail'),
]
