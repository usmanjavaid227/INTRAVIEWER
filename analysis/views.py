# The AnalysisView class performs emotion and sentiment analysis on a video file and saves the results
# to a database.
from django.shortcuts import render
from django.views import View
from .models import Interview
from django.http import HttpResponse
from .models import Analysis
import os

import cv2
from deepface import DeepFace
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
import moviepy.editor as mp

# Create your views here.

class AnalysisView(View):
     def get(self, request, interview_id):
        interview = Interview.objects.get(id=interview_id)

        return render(request, 'core/analysis.html', {'interview': interview})

     def post(self, request, interview_id):
        interview = Interview.objects.get(id=interview_id)
        video_file = interview.video_file.path

         # Open the video file
        cap = cv2.VideoCapture(str(video_file))

        # Analyze each frame
        emotions_list = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Analyze emotion for current frame
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection = False)
            
            # Save emotions for current frame
            emotions = result[0]['emotion']
            emotions = {k: v for k, v in sorted(emotions.items(), key=lambda item: item[1], reverse=True)}
            emotions = {k: v for k, v in emotions.items() if v > 0.1}
            emotions_list.append(emotions)

            

        # Release the capture and destroy windows
        cap.release()
        cv2.destroyAllWindows()

        emotions_total = {}
        emotions_count = len(emotions_list)
        for emotions in emotions_list:
            for k, v in emotions.items():
                if k not in emotions_total:
                    emotions_total[k] = 0
                emotions_total[k] += v

        emotions_total = {k: v/emotions_count for k, v in sorted(emotions_total.items(), key=lambda item: item[1], reverse=True)}
        emotions_total = {k: v for k, v in emotions_total.items() if v > 0.1}

        # analysis = Analysis(user=request.user, interview=interview, facial_expression=emotions_total)
        # analysis.save()

        # sentiment analysis

        # Extract the audio from the video file
        audio_file = 'audio.wav'
        clip = mp.VideoFileClip(video_file)
        clip.audio.write_audiofile(audio_file)
        
        # Perform speech recognition on the extracted audio
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio, language="en-US")
        
        # Perform sentiment analysis on the transcribed text
        sentences = [str(text)]
        analyzer = SentimentIntensityAnalyzer()
        for i in sentences:
            vs = analyzer.polarity_scores(i)
            print("{:-<65} {}".format(i, str(vs)))
         # Calculate the average sentiment score
        # avg_sentiment_score = sum(sentiment_scores) / len(sentiment_scores)

         # create feedback based on the sentiment score and emotion analysis
        if vs['compound'] >= 0.05 and emotions_total['happy'] >= 0.5:
            feedback = 'You did a great job! You seem very happy and confident.'
        elif vs['compound'] >= 0.05 and emotions_total['happy'] < 0.5:
            feedback = 'You did a good job! You seem confident.'
        elif vs['compound'] > -0.05 and vs['compound'] < 0.05 and emotions_total['happy'] >= 0.5:
            feedback = 'You did an okay job. You seem happy but not confident.'
        elif vs['compound'] > -0.05 and vs['compound'] < 0.05 and emotions_total['happy'] < 0.5:
            feedback = 'You did an okay job. You seem neither happy nor confident.'
        elif vs['compound'] <= -0.05 and emotions_total['happy'] >= 0.5:
            feedback = 'You did a poor job. You seem happy but not confident.'
        elif vs['compound'] <= -0.05 and emotions_total['happy'] < 0.5:
            feedback = 'You did a poor job. You seem neither happy nor confident.'
        else:
            feedback = 'Error calculating feedback.'

        
        # Save the analysis results
        analysis = Analysis(user=request.user, interview=interview, sentiment_score=vs,feedback=feedback, facial_expression=emotions_total)
        analysis.save()

        # delete the audio file
        os.remove(audio_file)
        
       

        # return HttpResponse('Analysis completed successfully!')
        return render(request, 'core/analysis.html', {'interview': interview, 'emotions': emotions_total, 'sentiment_score': vs, 'facial_expression':emotions_total, 'feedback':feedback})




