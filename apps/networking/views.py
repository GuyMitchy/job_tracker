from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import NetworkingContact, NetworkingEvent
from .forms import NetworkingContactForm, NetworkingEventForm

# Create your views here.

class ContactListView(LoginRequiredMixin, ListView):
    model = NetworkingContact
    template_name = 'networking/contact_list.html'
    context_object_name = 'contacts'

    def get_queryset(self):
        return NetworkingContact.objects.filter(user=self.request.user)

class ContactDetailView(LoginRequiredMixin, DetailView):
    model = NetworkingContact
    template_name = 'networking/contact_detail.html'
    context_object_name = 'contact'

    def get_queryset(self):
        return NetworkingContact.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = self.object.networkingevent_set.all().order_by('-event__start_time')
        return context

class ContactCreateView(LoginRequiredMixin, CreateView):
    model = NetworkingContact
    form_class = NetworkingContactForm
    template_name = 'networking/contact_form.html'
    success_url = reverse_lazy('networking:contact-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = NetworkingContact
    form_class = NetworkingContactForm
    template_name = 'networking/contact_form.html'

    def get_queryset(self):
        return NetworkingContact.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('networking:contact-detail', kwargs={'pk': self.object.pk})

class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = NetworkingContact
    template_name = 'networking/contact_confirm_delete.html'
    success_url = reverse_lazy('networking:contact-list')

    def get_queryset(self):
        return NetworkingContact.objects.filter(user=self.request.user)

class NetworkingEventListView(LoginRequiredMixin, ListView):
    model = NetworkingEvent
    template_name = 'networking/event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        return NetworkingEvent.objects.filter(contact__user=self.request.user)

class NetworkingEventCreateView(LoginRequiredMixin, CreateView):
    model = NetworkingEvent
    form_class = NetworkingEventForm
    template_name = 'networking/event_form.html'
    success_url = reverse_lazy('networking:event-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user to the form
        return kwargs

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['contact'].queryset = NetworkingContact.objects.filter(user=self.request.user)
        return form

    def form_valid(self, form):
        return super().form_valid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NetworkingEventDetailView(LoginRequiredMixin, DetailView):
    model = NetworkingEvent
    template_name = 'networking/event_detail.html'
    context_object_name = 'event'

    def get_queryset(self):
        return NetworkingEvent.objects.filter(contact__user=self.request.user)

class NetworkingEventUpdateView(LoginRequiredMixin, UpdateView):
    model = NetworkingEvent
    form_class = NetworkingEventForm
    template_name = 'networking/event_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user to the form
        return kwargs

    def get_queryset(self):
        return NetworkingEvent.objects.filter(contact__user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('networking:event-detail', kwargs={'pk': self.object.pk})
