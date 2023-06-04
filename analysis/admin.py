from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import Analysis

# Register your models here.
def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="report.csv"'

    writer = csv.writer(response)
    writer.writerow(['User', 'Created At', 'Sentiment Score', 'Facial Expression', 'Feedback'])

    for obj in queryset:
        writer.writerow([ obj.user.username, obj.created_at, obj.sentiment_score, obj.facial_expression, obj.feedback])

    return response
export_to_csv.short_description = 'Export to CSV'

class AnalysisAdmin(admin.ModelAdmin):
    list_display = ('user', 'interview', 'created_at', 'sentiment_score', 'facial_expression', 'feedback')
    actions = [export_to_csv]

admin.site.register(Analysis, AnalysisAdmin)
