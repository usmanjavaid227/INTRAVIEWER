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
    

# model for team 
class Team(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='team/')
    designation = models.CharField(max_length=200)
    description = models.TextField()
    fblink = models.URLField(max_length=200)
    twitterlink = models.URLField(max_length=200)
    instalink = models.URLField(max_length=200)
    linkedinlink = models.URLField(max_length=200)

    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='testimonial/')
    designation = models.CharField(max_length=200)
    feedback = models.TextField()

    def __str__(self):
        return self.name
    
