from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'start_time', 'end_time', 'is_all_day')
    list_filter = ('event_type', 'is_all_day')
    search_fields = ('title', 'description')
    date_hierarchy = 'start_time'
