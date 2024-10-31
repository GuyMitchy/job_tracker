from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from .models import LinkedInPost, LinkedInInteraction, LinkedInEngagementPlan
from .forms import LinkedInPostForm, LinkedInInteractionForm, LinkedInEngagementPlanForm

class LinkedInPostListView(LoginRequiredMixin, ListView):
    model = LinkedInPost
    template_name = 'linkedin/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return LinkedInPost.objects.filter(user=self.request.user).order_by('-posted_at')

class LinkedInPostCreateView(LoginRequiredMixin, CreateView):
    model = LinkedInPost
    form_class = LinkedInPostForm
    template_name = 'linkedin/post_form.html'
    success_url = reverse_lazy('linkedin:post-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class LinkedInPostDetailView(LoginRequiredMixin, DetailView):
    model = LinkedInPost
    template_name = 'linkedin/post_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        return LinkedInPost.objects.filter(user=self.request.user)

class LinkedInPostUpdateView(LoginRequiredMixin, UpdateView):
    model = LinkedInPost
    form_class = LinkedInPostForm
    template_name = 'linkedin/post_form.html'

    def get_success_url(self):
        return reverse_lazy('linkedin:post-detail', kwargs={'pk': self.object.pk})

class LinkedInInteractionListView(LoginRequiredMixin, ListView):
    model = LinkedInInteraction
    template_name = 'linkedin/interaction_list.html'
    context_object_name = 'interactions'

    def get_queryset(self):
        return LinkedInInteraction.objects.filter(user=self.request.user).order_by('-interaction_date')

class LinkedInInteractionCreateView(LoginRequiredMixin, CreateView):
    model = LinkedInInteraction
    form_class = LinkedInInteractionForm
    template_name = 'linkedin/interaction_form.html'
    success_url = reverse_lazy('linkedin:interaction-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class LinkedInEngagementPlanListView(LoginRequiredMixin, ListView):
    model = LinkedInEngagementPlan
    template_name = 'linkedin/plan_list.html'
    context_object_name = 'plans'

    def get_queryset(self):
        return LinkedInEngagementPlan.objects.filter(user=self.request.user).order_by('-start_date')

class LinkedInEngagementPlanCreateView(LoginRequiredMixin, CreateView):
    model = LinkedInEngagementPlan
    form_class = LinkedInEngagementPlanForm
    template_name = 'linkedin/plan_form.html'
    success_url = reverse_lazy('linkedin:plan-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) 