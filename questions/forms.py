from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'video_question']
        widgets = { 'text': forms.TextInput(attrs={'class': 'form-control'}), 'video_question': forms.FileInput(attrs={'class': 'form-control-file'})}
