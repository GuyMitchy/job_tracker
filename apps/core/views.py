from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from datetime import timedelta
from apps.applications.models import JobApplication
from apps.events.models import Event

# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        
        # Get upcoming events
        context['upcoming_events'] = Event.objects.filter(
            user=self.request.user,
            start_time__gte=now
        ).order_by('start_time')[:5]
        
        # Get recent applications
        context['recent_applications'] = JobApplication.objects.filter(
            user=self.request.user
        ).order_by('-application_date')[:5]
        
        # Calculate statistics
        context['active_applications'] = JobApplication.objects.filter(
            user=self.request.user,
            status__in=['applied', 'interviewing']
        ).count()
        
        context['interviews_this_week'] = Event.objects.filter(
            user=self.request.user,
            event_type='interview',
            start_time__gte=now,
            start_time__lte=now + timedelta(days=7)
        ).count()
        
        context['applications_this_month'] = JobApplication.objects.filter(
            user=self.request.user,
            application_date__month=now.month,
            application_date__year=now.year
        ).count()
        
        return context
