from django import forms
from .models import NetworkingContact, NetworkingEvent
from apps.events.models import Event

class NetworkingContactForm(forms.ModelForm):
    class Meta:
        model = NetworkingContact
        fields = ['name', 'company', 'position', 'email', 'phone', 'linkedin_url', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

class NetworkingEventForm(forms.ModelForm):
    start_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    end_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    
    class Meta:
        model = NetworkingEvent
        fields = ['contact', 'event_type', 'notes', 'follow_up_date']
        widgets = {
            'follow_up_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Create the associated Event
        event = Event.objects.create(
            user=self.user,
            title=f"{instance.get_event_type_display()} with {instance.contact.name}",
            event_type='networking',
            start_time=self.cleaned_data['start_time'],
            end_time=self.cleaned_data['end_time'],
            description=instance.notes
        )
        
        instance.event = event
        if commit:
            instance.save()
        return instance