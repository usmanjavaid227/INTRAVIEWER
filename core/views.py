from django.shortcuts import render
from .models import Card,Faq

# Create your views here.
def index(request):
    cards = Card.objects.all()
    faq= Faq.objects.all()
    context = {'cards': cards,'faq':faq}
    return render(request,'core/index.html',context)


def about(request):
    faq=Faq.objects.all()
    context={'faq':faq}
    return render(request,'core/about.html',context)
def contact(request):
    return render(request,'core/contact.html')
def feedback(request):
    return render(request,'core/feedback.html')
def history(request):
    return render(request,'core/history.html')
def interview(request):
    return render(request,'core/interview.html')
def services(request):
    cards = Card.objects.all()
    context = {'cards': cards}
    return render(request,'core/services.html',context)
def userindex(request):
    return render(request,'core/userindex.html')
def userprofile(request):
    return render(request,'core/userprofile.html')

def login(request):
    return render(request,'core/login.html')

def register(request):
    return render(request,'core/register.html')

def privacy(request):
    return render(request,'core/privacy_policy.html')
