from django import forms
from .models import LinkedInPost, LinkedInInteraction, LinkedInEngagementPlan
from apps.events.models import Event

class LinkedInPostForm(forms.ModelForm):
    class Meta:
        model = LinkedInPost
        fields = ['content', 'post_type', 'post_url', 'posted_at']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
            'posted_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
            # Create calendar event for post
            Event.objects.create(
                user=user,
                title=f"LinkedIn Post: {instance.get_post_type_display()}",
                event_type='linkedin',
                start_time=instance.posted_at,
                end_time=instance.posted_at,
                description=instance.content[:200],
                is_all_day=True
            )
        return instance

class LinkedInInteractionForm(forms.ModelForm):
    class Meta:
        model = LinkedInInteraction
        fields = ['contact_name', 'contact_title', 'contact_company', 
                 'contact_url', 'interaction_type', 'notes', 
                 'interaction_date', 'follow_up_needed', 'follow_up_date']
        widgets = {
            'interaction_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'follow_up_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

class LinkedInEngagementPlanForm(forms.ModelForm):
    class Meta:
        model = LinkedInEngagementPlan
        fields = ['title', 'description', 'target_connections', 
                 'target_posts', 'target_interactions', 'frequency',
                 'start_date', 'end_date']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        } 