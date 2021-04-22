from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from base.models import Task
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('task-list')

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name="task_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = context['task_list'].filter(user=self.request.user)
        context['count'] = context['task_list'].filter(complete_status=False)
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name='task'
    template_name='base/task_detail.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete_status']
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete_status']
    success_url = reverse_lazy('task-list')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name='task'
    success_url = reverse_lazy('task-list')