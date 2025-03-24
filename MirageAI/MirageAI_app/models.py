from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Will be hashed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class AIProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ai_profiles")
    voice_url = models.URLField()
    personality_traits = models.JSONField()  # Stores AI personality details
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AI Profile of {self.user.name}"

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chats")
    ai_profile = models.ForeignKey(AIProfile, on_delete=models.CASCADE, related_name="chats")
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat with {self.ai_profile} on {self.timestamp}"

class VoiceClone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="voice_clones")
    audio_file = models.FileField(upload_to="voice_clones/")
    processed_audio = models.FileField(upload_to="processed_voices/", null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Voice Clone of {self.user.name}"

