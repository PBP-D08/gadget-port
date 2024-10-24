from django.db import models

class MoodEntry(models.Model):
    mood = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    feelings = models.TextField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5