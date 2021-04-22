from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from base.models import Task
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('task-list')

class TaskList(ListView):
    model = Task
    context_object_name="task_list"

class TaskDetail(DetailView):
    model = Task
    context_object_name='task'
    template_name='base/task_detail.html'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')

class TaskDelete(DeleteView):
    model = Task
    context_object_name='task'
    success_url = reverse_lazy('task-list')