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
        
        def save(self, commit=True):
            analysis = super().save(commit=False)
            if analysis.sentiment_score >= 0.7 and analysis.facial_expression == "confident":
                analysis.feedback = "Great job! You came across as confident and knowledgeable in your responses. Keep up the good work."
            elif analysis.sentiment_score < 0.7 and analysis.facial_expression == "neutral":
                analysis.feedback = "It seems like you could work on being more enthusiastic and engaged in your responses. Practice answering questions with more energy and enthusiasm."
            else:
                analysis.feedback = "Your interview performance was good overall. Consider working on improving your responses to some of the more challenging questions."
            if commit:
                analysis.save()
            return analysis