from django.db import models
from django.conf import settings
from apps.applications.models import JobApplication
from apps.networking.models import NetworkingEvent

# Create your models here.

class JobSearchMetrics(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    applications_submitted = models.PositiveIntegerField(default=0)
    interviews_attended = models.PositiveIntegerField(default=0)
    networking_events = models.PositiveIntegerField(default=0)
    offers_received = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'analytics'
        ordering = ['-date']
        unique_together = ['user', 'date']

    def __str__(self):
        return f"Metrics for {self.user.username} - {self.date}"

class ActivityLog(models.Model):
    ACTION_TYPES = [
        ('application', 'Job Application'),
        ('status_change', 'Application Status Change'),
        ('networking', 'Networking Activity'),
        ('interview', 'Interview'),
        ('offer', 'Job Offer'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=20, choices=ACTION_TYPES)
    description = models.TextField()
    job_application = models.ForeignKey(
        JobApplication, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    networking_event = models.ForeignKey(
        NetworkingEvent, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'analytics'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.action_type} - {self.created_at.date()}"
