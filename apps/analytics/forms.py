from django import forms
from .models import JobSearchMetrics

class JobSearchMetricsForm(forms.ModelForm):
    class Meta:
        model = JobSearchMetrics
        fields = ['date', 'applications_submitted', 'interviews_attended', 
                 'networking_events', 'offers_received']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        } 