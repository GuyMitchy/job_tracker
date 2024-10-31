from django.db import models
from django.conf import settings
from apps.events.models import Event

# Create your models here.

class NetworkingContact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    linkedin_url = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'networking'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.company}"

class NetworkingEvent(models.Model):
    EVENT_TYPES = [
        ('coffee', 'Coffee Chat'),
        ('interview', 'Informational Interview'),
        ('call', 'Phone Call'),
        ('meetup', 'Meetup'),
        ('conference', 'Conference'),
        ('other', 'Other'),
    ]

    contact = models.ForeignKey(NetworkingContact, on_delete=models.CASCADE)
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    notes = models.TextField(blank=True)
    follow_up_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'networking'
        ordering = ['-event__start_time']

    def __str__(self):
        return f"{self.event_type} with {self.contact.name}"
