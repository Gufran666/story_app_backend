from django.db import models

class Story(models.Model):
    prompt = models.CharField(max_length=255)
    full_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Story: {self.prompt[:50]}"