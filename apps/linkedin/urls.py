from django.urls import path
from . import views

app_name = 'linkedin'

urlpatterns = [
    path('posts/', views.LinkedInPostListView.as_view(), name='post-list'),
    path('posts/create/', views.LinkedInPostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.LinkedInPostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', views.LinkedInPostUpdateView.as_view(), name='post-edit'),
    path('interactions/', views.LinkedInInteractionListView.as_view(), name='interaction-list'),
    path('interactions/create/', views.LinkedInInteractionCreateView.as_view(), name='interaction-create'),
    path('plan/', views.LinkedInEngagementPlanListView.as_view(), name='plan-list'),
    path('plan/create/', views.LinkedInEngagementPlanCreateView.as_view(), name='plan-create'),
] 