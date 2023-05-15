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
    
# class RecorderView(View):
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return redirect('login') 
#         return super().dispatch(request, *args, **kwargs)
    
#     def get(self, request):
#         recorder = Recorder('interview_videos')
#         recorder.startRecording()
#         try: 
#             while True:
#                 cv2.waitKey(1)
#         except KeyboardInterrupt:
#             recorder.stopRecording()
#             return redirect('interview')
