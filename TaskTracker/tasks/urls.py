from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('ekle/', views.task_create, name='task_create'),
    path('completed/', views.completed_tasks, name='completed_tasks'),
]
