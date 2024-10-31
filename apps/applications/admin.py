from django.contrib import admin
from .models import Company, JobApplication

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry', 'website')
    search_fields = ('name', 'industry')

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'status', 'application_date')
    list_filter = ('status', 'application_date')
    search_fields = ('position', 'company__name')
    date_hierarchy = 'application_date'
