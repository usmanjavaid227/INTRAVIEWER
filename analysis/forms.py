from django import forms
from .models import Analysis

class AnalysisForm(forms.ModelForm):
     class Meta:
        model = Analysis
        fields = ['sentiment_score', 'facial_expression', 'feedback']
        widgets = {
            'sentiment_score': forms.HiddenInput(),
            'facial_expression': forms.HiddenInput(),
            'feedback': forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
        }
        