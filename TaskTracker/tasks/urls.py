from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('ekle/', views.task_create, name='task_create'),
    path('completed/', views.completed_tasks, name='completed_tasks'),
    path('task/<int:pk>/edit/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('task/<int:id>/complete/', views.complete_task, name='complete_task'),
    path('ongoing/', views.ongoing_tasks, name='ongoing_tasks'),
]
