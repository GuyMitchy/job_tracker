from django.contrib import admin
from .models import JobSearchMetrics, ActivityLog

@admin.register(JobSearchMetrics)
class JobSearchMetricsAdmin(admin.ModelAdmin):
    list_display = ('date', 'applications_submitted', 'interviews_attended', 'offers_received')
    date_hierarchy = 'date'
    list_filter = ('date',)

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('action_type', 'created_at', 'user')
    list_filter = ('action_type', 'created_at')
    search_fields = ('description',)
    date_hierarchy = 'created_at'
