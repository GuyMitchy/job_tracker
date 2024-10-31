from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Goal, GoalProgress
from .forms import GoalForm, GoalProgressForm

class GoalListView(LoginRequiredMixin, ListView):
    model = Goal
    template_name = 'targets/goal_list.html'
    context_object_name = 'goals'

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user).order_by('-start_date')

class GoalDetailView(LoginRequiredMixin, DetailView):
    model = Goal
    template_name = 'targets/goal_detail.html'
    context_object_name = 'goal'

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['progress_entries'] = self.object.progress.all().order_by('-date')
        return context

class GoalCreateView(LoginRequiredMixin, CreateView):
    model = Goal
    form_class = GoalForm
    template_name = 'targets/goal_form.html'
    success_url = reverse_lazy('targets:goal-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GoalUpdateView(LoginRequiredMixin, UpdateView):
    model = Goal
    form_class = GoalForm
    template_name = 'targets/goal_form.html'

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('targets:goal-detail', kwargs={'pk': self.object.pk})

class GoalDeleteView(LoginRequiredMixin, DeleteView):
    model = Goal
    template_name = 'targets/goal_confirm_delete.html'
    success_url = reverse_lazy('targets:goal-list')

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

class GoalProgressCreateView(LoginRequiredMixin, CreateView):
    model = GoalProgress
    form_class = GoalProgressForm
    template_name = 'targets/progress_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.goal = get_object_or_404(Goal, pk=kwargs['goal_pk'], user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['goal'] = self.goal  # Pass the goal to the form
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goal'] = self.goal
        return context

    def form_valid(self, form):
        form.instance.goal = self.goal
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('targets:goal-detail', kwargs={'pk': self.goal.pk})

class GoalProgressUpdateView(LoginRequiredMixin, UpdateView):
    model = GoalProgress
    form_class = GoalProgressForm
    template_name = 'targets/progress_form.html'

    def get_queryset(self):
        return GoalProgress.objects.filter(goal__user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('targets:goal-detail', kwargs={'pk': self.object.goal.pk})
