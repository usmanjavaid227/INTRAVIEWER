from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'core/index.html')
def about(request):
    return render(request,'core/about.html')
def contact(request):
    return render(request,'core/contact.html')
def feedback(request):
    return render(request,'core/feedback.html')
def history(request):
    return render(request,'core/history.html')
def interview(request):
    return render(request,'core/interview.html')
def services(request):
    return render(request,'core/services.html')
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
