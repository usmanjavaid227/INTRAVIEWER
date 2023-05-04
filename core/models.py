from django.db import models

# Create your models here.

class Card(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='cards/')

    def __str__(self):
        return self.title

# model for faq
class Faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField(max_length=300)

    def __str__(self):
        return self.question
    