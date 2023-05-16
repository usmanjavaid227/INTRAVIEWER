from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from questions.models import Question
from .Recorder import Recorder
import time
import cv2

# Create your views here.

class InterviewView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login') 
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        questions = Question.objects.all()
        return render(request, 'core/interview.html', {'questions': questions})
    
    def post(self, request):
            recorder = Recorder('interivew')
            recorder.startRecording()
            time.sleep(5)
            recorder.stopRecording()
            recorder.saveRecording()

            return render(request, 'core/history.html')
