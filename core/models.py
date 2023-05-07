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
    

countries = (
    ('AF', 'Afghanistan'),
    ('AL', 'Albania'),
    ('BZ', 'Belize'),
    ('IN', 'India'),
    ('US', 'United States'),
    ('GB', 'United Kingdom'),
    ('CA', 'Canada'),
    ('AU', 'Australia'),
    ('DE', 'Germany'),
    ('FR', 'France'),
    ('IT', 'Italy'),
    ('ES', 'Spain'),
    ('RU', 'Russia'),
    ('CN', 'China'),
    ('JP', 'Japan'),
    ('BR', 'Brazil'),
    ('MX', 'Mexico'),
    ('AR', 'Argentina'),
    ('PK', 'Pakistan'),
    ('EG', 'Egypt'),
    ('NZ', 'New Zealand'),
    ('ZA', 'South Africa'),
    ('BD', 'Bangladesh'),

)

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    country = models.CharField(max_length=2, choices=countries, default='US')
    destination = models.CharField(max_length=50, blank=True)
    linkedin_url = models.URLField(blank=True)
    bio = models.TextField(max_length=500, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    Dream_Job = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='profile_pics', default='', blank=True)
    address= models.CharField(max_length=100, blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'
    
