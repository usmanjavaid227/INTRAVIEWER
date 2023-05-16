from django.contrib import admin
from .models import Interview
import os

# Register your models here.
@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'video_file', 'created_at')

    def delete_model(self, request, obj):
        # Delete the associated video file
        if obj.video_file:
            path = obj.video_file.path
            if os.path.isfile(path):
                os.remove(path)
        
        # Call the superclass delete_model method
        super().delete_model(request, obj)