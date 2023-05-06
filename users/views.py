from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views import View
from .forms import RegisterForm


# Create your views here.
class CustomerRegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'Invalid data!')
            return render(request, 'users/register.html', {'form': form})
    
    def get_context_data(self, **kwargs):
        kwargs['title'] = 'Customer Registration'
        return super().get_context_data(**kwargs)



    




