from django import forms
from .models import Goal, GoalProgress

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'description', 'goal_type', 'period', 
                 'target_number', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("End date must be after start date.")
        
        return cleaned_data

class GoalProgressForm(forms.ModelForm):
    class Meta:
        model = GoalProgress
        fields = ['date', 'actual_number', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        self.goal = kwargs.pop('goal', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        goal = self.goal

        if goal and date:
            if date < goal.start_date or date > goal.end_date:
                raise forms.ValidationError(
                    "Progress date must be within the goal's date range."
                )
        
        return cleaned_data 