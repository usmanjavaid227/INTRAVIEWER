from django.contrib import admin
from django.urls import path
from core.views import (IndexView, AboutView, ContactView, FeedbackView,
                         ServicesView, UserIndexView, ProfileView, PrivacyView)
from interview.views import InterviewView, HistoryView
from django.conf.urls.static import static
from mainapp import settings
from interview import views
from analysis.views import AnalysisView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('history/', HistoryView.as_view(), name='history'),
    path('interview/', InterviewView.as_view(), name='interview'),
    path('interview/<int:interview_id>/delete/', views.delete_interview, name='delete_interview'),
    path('interview/<int:interview_id>/', AnalysisView.as_view(), name='analysis'),
    path('services/', ServicesView.as_view(), name='services'),
    path('userindex/', UserIndexView.as_view(), name='userindex'),
    path('userprofile/', ProfileView.as_view(), name='userprofile'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
