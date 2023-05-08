from django import forms
from .models import Interview

class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['question', 'video_file']
        labels = { 'question': 'Question', 'video_file': 'Video File' }
        widgets = { 'question': forms.HiddenInput() }

