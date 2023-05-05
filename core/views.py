from django.views import View
from django.shortcuts import render
from .models import Card, Faq, Team, Testimonial

class IndexView(View):
    def get(self, request):
        cards = Card.objects.all()
        faq = Faq.objects.all()
        testimonial = Testimonial.objects.all()
        context = {'cards': cards, 'faq': faq, 'testimonial': testimonial}
        return render(request, 'core/index.html', context)


class AboutView(View):
    def get(self, request):
        faq = Faq.objects.all()
        team = Team.objects.all()
        context = {'faq': faq, 'team': team}
        return render(request, 'core/about.html', context)


class ContactView(View):
    def get(self, request):
        return render(request, 'core/contact.html')


class FeedbackView(View):
    def get(self, request):
        return render(request, 'core/feedback.html')


class HistoryView(View):
    def get(self, request):
        return render(request, 'core/history.html')


class InterviewView(View):
    def get(self, request):
        return render(request, 'core/interview.html')


class ServicesView(View):
    def get(self, request):
        cards = Card.objects.all()
        context = {'cards': cards}
        return render(request, 'core/services.html', context)


class UserIndexView(View):
    def get(self, request):
        return render(request, 'core/userindex.html')


class UserProfileView(View):
    def get(self, request):
        return render(request, 'core/userprofile.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'core/login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'core/register.html')


class PrivacyView(View):
    def get(self, request):
        return render(request, 'core/privacy_policy.html')
