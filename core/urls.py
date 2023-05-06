from django.contrib import admin
from django.urls import path
from core.views import (IndexView, AboutView, ContactView, FeedbackView, HistoryView,
                        InterviewView, ServicesView, UserIndexView, UserProfileView, PrivacyView)
from django.conf.urls.static import static
from mainapp import settings

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('history/', HistoryView.as_view(), name='history'),
    path('interview/', InterviewView.as_view(), name='interview'),
    path('services/', ServicesView.as_view(), name='services'),
    path('userindex/', UserIndexView.as_view(), name='userindex'),
    path('userprofile/', UserProfileView.as_view(), name='userprofile'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
