from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core import views
from .views import CustomerRegisterView
from django.contrib.auth import views as auth_views
from users.forms import LoginForm, ChangePasswordForm, ResetPasswordForm, SetNewPasswordForm

urlpatterns = [
    path('register/', CustomerRegisterView.as_view(), name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='users/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='users/password_change.html', form_class=ChangePasswordForm,success_url='/password_change_done/'), name='passwordchange'),
    path('passwordchange/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html',form_class=ResetPasswordForm), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',form_class=SetNewPasswordForm), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),


    # path('profile/', views.ProfileView.as_view(template_name='core/userprofile.html'), name='profile'),
         
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)