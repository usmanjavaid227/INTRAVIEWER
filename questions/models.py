from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text