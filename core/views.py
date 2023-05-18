from django.views import View
from django.shortcuts import render
from .models import Card, Faq, Team, Testimonial
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import ContactForm
from .forms import UserForm, ProfileForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from analysis.models import Analysis
from interview.models import Interview
from core.models import Profile


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
        # result of last analysis of user 
        analysis = Analysis.objects.filter(user=request.user).last()
        total_interview = Interview.objects.filter(user=request.user).count()
        interviews = Interview.objects.filter(user=request.user)

# This is a Django model class for a user profile with various fields such as gender, country,
# destination, bio, date of birth, dream job, phone, image, and address.
        context = {'user': user, 'analysis': analysis, 'total_interview': total_interview, 'interviews': interviews }
        return render(request, 'core/userindex.html', context)
    

class ProfileView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login') 
        return super().dispatch(request, *args, **kwargs)
    def get(self, request):
        try:
            profile = request.user.profile
        except ObjectDoesNotExist:
            profile = None
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
        return render(request, 'core/userprofile.html', {'userprofile': user_form, 'profileform': profile_form})
    
    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        try:
            profile = request.user.profile
        except ObjectDoesNotExist:
            profile = Profile(user=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('userprofile')
        else:
            messages.error(request, 'Please correct the error below.')
            return render(request, 'core/userprofile.html', {'userform': user_form, 'profileform': profile_form})
        


class PrivacyView(View):
    def get(self, request):
        return render(request, 'core/privacy_policy.html')
