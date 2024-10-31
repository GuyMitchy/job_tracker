from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    linkedin_profile = models.URLField(blank=True)
    job_title = models.CharField(max_length=100, blank=True)
    industry = models.CharField(max_length=100, blank=True)
    
    class Meta:
        app_label = 'users'
