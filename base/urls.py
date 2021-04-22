from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views as base_views

urlpatterns = [
    path('login/', base_views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', base_views.RegisterPage.as_view(), name='register'),


    path('', base_views.TaskList.as_view(), name='task-list'),
    path('task/<int:pk>/', base_views.TaskDetail.as_view(), name='task'),
    path('task-create/', base_views.TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', base_views.TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', base_views.TaskDelete.as_view(), name='task-delete'),
]
