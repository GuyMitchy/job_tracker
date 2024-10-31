from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from datetime import timedelta
from apps.applications.models import JobApplication
from apps.events.models import Event
from apps.targets.models import Goal
from apps.networking.models import NetworkingEvent
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        
        # Get events and serialize them for the calendar
        events = Event.objects.filter(
            user=self.request.user,
            start_time__gte=now - timedelta(days=30),
            start_time__lte=now + timedelta(days=60)
        ).select_related('user')

        calendar_events = []
        for event in events:
            calendar_events.append({
                'id': event.id,
                'title': event.title,
                'start': event.start_time.isoformat(),
                'end': event.end_time.isoformat(),
                'className': f'fc-event-{event.event_type}',
                'allDay': event.is_all_day,
                'extendedProps': {
                    'type': event.event_type,
                    'description': event.description
                }
            })

        context['calendar_events_json'] = json.dumps(calendar_events, cls=DjangoJSONEncoder)
        
        # Applications for calendar
        context['applications'] = JobApplication.objects.filter(
            user=self.request.user,
            application_date__gte=now - timedelta(days=30)
        )
        
        # Goals for calendar
        context['goals'] = Goal.objects.filter(
            user=self.request.user,
            end_date__gte=now
        )
        
        # Upcoming events
        context['upcoming_events'] = Event.objects.filter(
            user=self.request.user,
            start_time__gte=now
        ).order_by('start_time')[:5]
        
        # Statistics
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
        
        context['networking_events_count'] = NetworkingEvent.objects.filter(
            contact__user=self.request.user,
            event__start_time__gte=now
        ).count()
        
        return context
