from django.urls import path
from . import views

app_name = 'networking'

urlpatterns = [
    path('contacts/', views.ContactListView.as_view(), name='contact-list'),
    path('contacts/create/', views.ContactCreateView.as_view(), name='contact-create'),
    path('contacts/<int:pk>/', views.ContactDetailView.as_view(), name='contact-detail'),
    path('contacts/<int:pk>/edit/', views.ContactUpdateView.as_view(), name='contact-edit'),
    path('contacts/<int:pk>/delete/', views.ContactDeleteView.as_view(), name='contact-delete'),
    path('event/', views.NetworkingEventListView.as_view(), name='event-list'),
    path('event/create/', views.NetworkingEventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/', views.NetworkingEventDetailView.as_view(), name='event-detail'),
    path('event/<int:pk>/edit/', views.NetworkingEventUpdateView.as_view(), name='event-edit'),
] 