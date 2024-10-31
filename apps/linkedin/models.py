from django.db import models
from django.conf import settings
from apps.events.models import Event

class LinkedInPost(models.Model):
    POST_TYPES = [
        ('article', 'Article Share'),
        ('update', 'Status Update'),
        ('achievement', 'Achievement'),
        ('job_search', 'Job Search Update'),
        ('project', 'Project Showcase'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    post_type = models.CharField(max_length=20, choices=POST_TYPES)
    post_url = models.URLField(blank=True)
    posted_at = models.DateTimeField()
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    event = models.OneToOneField(Event, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_post_type_display()} - {self.posted_at.date()}"

class LinkedInInteraction(models.Model):
    INTERACTION_TYPES = [
        ('connection', 'Connection Request'),
        ('message', 'Message'),
        ('comment', 'Comment'),
        ('like', 'Like'),
        ('share', 'Share'),
        ('follow', 'Follow'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=100)
    contact_title = models.CharField(max_length=100, blank=True)
    contact_company = models.CharField(max_length=100, blank=True)
    contact_url = models.URLField(blank=True)
    interaction_type = models.CharField(max_length=20, choices=INTERACTION_TYPES)
    notes = models.TextField(blank=True)
    interaction_date = models.DateTimeField()
    follow_up_needed = models.BooleanField(default=False)
    follow_up_date = models.DateField(null=True, blank=True)
    event = models.OneToOneField(Event, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_interaction_type_display()} with {self.contact_name}"

class LinkedInEngagementPlan(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('biweekly', 'Bi-Weekly'),
        ('monthly', 'Monthly'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    target_connections = models.IntegerField(default=0)
    target_posts = models.IntegerField(default=0)
    target_interactions = models.IntegerField(default=0)
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.frequency})" 