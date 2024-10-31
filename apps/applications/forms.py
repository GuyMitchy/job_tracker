from django import forms
from .models import JobApplication, Company

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['company', 'position', 'job_description', 'salary_range', 
                 'application_date', 'status', 'application_url']
        widgets = {
            'application_date': forms.DateInput(attrs={'type': 'date'}),
            'job_description': forms.Textarea(attrs={'rows': 4}),
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'website', 'industry', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        } 