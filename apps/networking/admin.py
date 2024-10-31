from django.contrib import admin
from .models import NetworkingContact, NetworkingEvent

@admin.register(NetworkingContact)
class NetworkingContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'position', 'email')
    search_fields = ('name', 'company', 'position')
    list_filter = ('company',)

@admin.register(NetworkingEvent)
class NetworkingEventAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'contact', 'follow_up_date')
    list_filter = ('event_type', 'follow_up_date')
    search_fields = ('contact__name', 'notes')
    date_hierarchy = 'created_at'
