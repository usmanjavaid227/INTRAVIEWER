from django.views import View
from django.shortcuts import render
from .models import Card, Faq, Team, Testimonial
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages


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
        form = ContactForm()
        return render(request, 'core/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f'New contact form submission from {name}',
                f'{message}\n\nFrom: {name} ({email})',
                f'{email}', # replace with your email address
                ['usmanjavaid227@gmail.com'], # replace with the recipient email address(es)
                fail_silently=False,
            )
            message = messages.success(request, 'Your message has been sent!')
            return HttpResponseRedirect('/contact/', {'message': message})
        else:
            return render(request, 'core/contact.html', {'form': form})


class FeedbackView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login') # replace 'login' with the name of your login page url
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'core/feedback.html')


class HistoryView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login') # replace 'login' with the name of your login page url
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'core/history.html')


class InterviewView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login') # replace 'login' with the name of your login page url
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'core/interview.html')


class ServicesView(View):
    def get(self, request):
        cards = Card.objects.all()
        context = {'cards': cards}
        return render(request, 'core/services.html', context)


class UserIndexView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login') # replace 'login' with the name of your login page url
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        user = User.objects.get(username=request.user.username)
        context = {'user': user}
        return render(request, 'core/userindex.html', context)


class UserProfileView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login') # replace 'login' with the name of your login page url
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'core/userprofile.html')

# class UserProfileView(View):
#     def get(self, request):
#         user = User.objects.get(username=request.user.username)
#         context = {'user': user}
#         return render(request, 'core/userprofile.html', context)



class PrivacyView(View):
    def get(self, request):
        return render(request, 'core/privacy_policy.html')
