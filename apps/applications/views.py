from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from .models import JobApplication, Company
from .forms import JobApplicationForm, CompanyForm

# Create your views here.

class JobApplicationListView(LoginRequiredMixin, ListView):
    model = JobApplication
    template_name = 'applications/application_list.html'
    context_object_name = 'applications'
    
    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user).order_by('-application_date')

class JobApplicationCreateView(LoginRequiredMixin, CreateView):
    model = JobApplication
    form_class = JobApplicationForm
    template_name = 'applications/application_form.html'
    success_url = reverse_lazy('applications:list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JobApplicationDetailView(LoginRequiredMixin, DetailView):
    model = JobApplication
    template_name = 'applications/application_detail.html'
    context_object_name = 'application'

    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)

class JobApplicationUpdateView(LoginRequiredMixin, UpdateView):
    model = JobApplication
    form_class = JobApplicationForm
    template_name = 'applications/application_form.html'
    
    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('applications:detail', kwargs={'pk': self.object.pk})

class JobApplicationDeleteView(LoginRequiredMixin, DeleteView):
    model = JobApplication
    template_name = 'applications/application_confirm_delete.html'
    success_url = reverse_lazy('applications:list')
    
    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)

class CompanyListView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'applications/company_list.html'
    context_object_name = 'companies'

class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'applications/company_form.html'
    success_url = reverse_lazy('applications:company-list')
