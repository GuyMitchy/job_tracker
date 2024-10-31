from django.urls import path
from . import views

app_name = 'targets'

urlpatterns = [
    path('', views.GoalListView.as_view(), name='goal-list'),
    path('create/', views.GoalCreateView.as_view(), name='goal-create'),
    path('<int:pk>/', views.GoalDetailView.as_view(), name='goal-detail'),
    path('<int:pk>/edit/', views.GoalUpdateView.as_view(), name='goal-edit'),
    path('<int:pk>/delete/', views.GoalDeleteView.as_view(), name='goal-delete'),
    path('<int:goal_pk>/progress/add/', views.GoalProgressCreateView.as_view(), name='progress-create'),
    path('progress/<int:pk>/edit/', views.GoalProgressUpdateView.as_view(), name='progress-edit'),
] 