from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('', views.AnalyticsDashboardView.as_view(), name='dashboard'),
    path('metrics/', views.MetricsListView.as_view(), name='metrics-list'),
    path('metrics/create/', views.MetricsCreateView.as_view(), name='metrics-create'),
    path('activity-log/', views.ActivityLogListView.as_view(), name='activity-log'),
] 