from django.contrib import admin

# Register your models here.
from .models import Card,Faq,Team,Testimonial,Profile

admin.site.register(Card)
admin.site.register(Faq)
admin.site.register(Team)
admin.site.register(Testimonial)
admin.site.register(Profile)






