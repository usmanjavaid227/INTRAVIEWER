from django.db import models
from django.contrib.auth.models import User
from interview.models import Interview

class Analysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    sentiment_score = models.FloatField(null=True, blank=True)
    facial_expression = models.CharField(max_length=50, null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username + " - " + self.interview.title + " - " + str(self.created_at) + " - " + str(self.sentiment_score) + " - " + self.facial_expression + " - " + self.feedback 