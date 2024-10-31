from django.db import models
from django.conf import settings
from apps.events.models import Event

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    industry = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "companies"
        app_label = 'applications'

    def __str__(self):
        return self.name

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('saved', 'Saved'),
        ('applied', 'Applied'),
        ('interviewing', 'Interviewing'),
        ('offered', 'Offered'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    job_description = models.TextField(blank=True)
    salary_range = models.CharField(max_length=100, blank=True)
    application_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='saved')
    application_url = models.URLField(blank=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.position} at {self.company.name}"

    class Meta:
        app_label = 'applications'
