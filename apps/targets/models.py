from django.db import models
from django.conf import settings

# Create your models here.

class Goal(models.Model):
    PERIOD_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
    ]
    
    TYPE_CHOICES = [
        ('applications', 'Job Applications'),
        ('networking', 'Networking Events'),
        ('interviews', 'Interviews'),
        ('skills', 'Skills Development'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    goal_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    period = models.CharField(max_length=20, choices=PERIOD_CHOICES)
    target_number = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'targets'
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.title} ({self.period})"

class GoalProgress(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='progress')
    date = models.DateField()
    actual_number = models.PositiveIntegerField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'targets'
        ordering = ['-date']
        unique_together = ['goal', 'date']

    def __str__(self):
        return f"{self.goal.title} - {self.date}"
