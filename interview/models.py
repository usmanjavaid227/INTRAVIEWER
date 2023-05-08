from django.db import models
from django.contrib.auth.models import User
from questions.models import Question

# Create your models here.

class Interview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='interview_videos')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.question.text}"
    