from django.contrib import admin 
from .models import User, AIProfile, Chat, VoiceClone

admin.site.register(User)
admin.site.register(AIProfile)
admin.site.register(Chat)
admin.site.register(VoiceClone)

