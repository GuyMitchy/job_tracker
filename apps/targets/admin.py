from django.contrib import admin
from .models import Goal, GoalProgress

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'goal_type', 'period', 'target_number', 'start_date', 'end_date')
    list_filter = ('goal_type', 'period')
    search_fields = ('title', 'description')
    date_hierarchy = 'start_date'

@admin.register(GoalProgress)
class GoalProgressAdmin(admin.ModelAdmin):
    list_display = ('goal', 'date', 'actual_number')
    list_filter = ('date',)
    date_hierarchy = 'date'
