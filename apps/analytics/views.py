from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.db.models import Count
from datetime import timedelta
from .models import JobSearchMetrics, ActivityLog
from .forms import JobSearchMetricsForm
from apps.applications.models import JobApplication
from apps.networking.models import NetworkingEvent

# Create your views here.

class AnalyticsDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'analytics/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        thirty_days_ago = now - timedelta(days=30)
        
        # Application statistics
        applications = JobApplication.objects.filter(user=self.request.user)
        context['total_applications'] = applications.count()
        context['active_applications'] = applications.filter(
            status__in=['applied', 'interviewing']
        ).count()
        context['success_rate'] = (
            applications.filter(status='offered').count() / applications.count() * 100
            if applications.count() > 0 else 0
        )
        
        # Application status breakdown
        status_counts = applications.values('status').annotate(
            count=Count('status')
        ).order_by('status')
        context['status_breakdown'] = status_counts
        
        # Recent activity
        context['recent_activity'] = ActivityLog.objects.filter(
            user=self.request.user
        ).select_related('job_application', 'networking_event')[:10]
        
        # Monthly trends
        context['monthly_metrics'] = JobSearchMetrics.objects.filter(
            user=self.request.user,
            date__gte=thirty_days_ago
        ).order_by('date')
        
        return context

class MetricsListView(LoginRequiredMixin, ListView):
    model = JobSearchMetrics
    template_name = 'analytics/metrics_list.html'
    context_object_name = 'metrics'
    
    def get_queryset(self):
        return JobSearchMetrics.objects.filter(
            user=self.request.user
        ).order_by('-date')

class MetricsCreateView(LoginRequiredMixin, CreateView):
    model = JobSearchMetrics
    form_class = JobSearchMetricsForm
    template_name = 'analytics/metrics_form.html'
    success_url = reverse_lazy('analytics:metrics-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ActivityLogListView(LoginRequiredMixin, ListView):
    model = ActivityLog
    template_name = 'analytics/activity_log.html'
    context_object_name = 'activities'
    paginate_by = 20
    
    def get_queryset(self):
        return ActivityLog.objects.filter(
            user=self.request.user
        ).select_related('job_application', 'networking_event')
