from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from questions.models import Question
from .Recorder import Recorder
import time
from django.core.files import File
from .models import Interview
from django.http import HttpResponse

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
            time.sleep(30)
            recorder.stopRecording()
            recorder.saveRecording()

            video_path = 'media/temp/interivew.mp4'
            with open(video_path, 'rb') as video_file:
                 django_file = File(video_file)
                 interview = Interview()
                 interview.user = request.user
                 interview.video_file.save('interview.mp4', django_file, save=True)
                 interview.save()
            
            return redirect('history')


class HistoryView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        interviews = Interview.objects.filter(user=request.user)
        return render(request, 'core/history.html', {'interviews': interviews})
def delete_interview(request, interview_id):
    if request.method == 'POST':
        try:
            interview = Interview.objects.get(id=interview_id)
            # Delete the video file from the media storage
            interview.video_file.delete()
            # Delete the interview object from the database
            interview.delete()
            return redirect('history')  # Redirect to the history page after deletion
        except Interview.DoesNotExist:
            pass
    return redirect('history') 
    

