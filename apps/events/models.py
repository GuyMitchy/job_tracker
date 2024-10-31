from django.db import models
from django.conf import settings

# Create your models here.

class Event(models.Model):
    EVENT_TYPES = [
        ('application', 'Job Application'),
        ('interview', 'Interview'),
        ('networking', 'Networking'),
        ('followup', 'Follow Up'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    is_all_day = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'events'
        ordering = ['-start_time']

    def __str__(self):
        return f"{self.title} - {self.start_time.date()}"
