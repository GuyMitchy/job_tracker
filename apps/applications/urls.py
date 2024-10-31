from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('', views.JobApplicationListView.as_view(), name='list'),
    path('create/', views.JobApplicationCreateView.as_view(), name='create'),
    path('<int:pk>/', views.JobApplicationDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.JobApplicationUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.JobApplicationDeleteView.as_view(), name='delete'),
    path('companies/', views.CompanyListView.as_view(), name='company-list'),
    path('companies/create/', views.CompanyCreateView.as_view(), name='company-create'),
] 