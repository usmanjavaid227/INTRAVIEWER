from django import forms
from .models import Interview

class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = [ 'video_file']
        labels = {  'video_file': 'Video File' }

