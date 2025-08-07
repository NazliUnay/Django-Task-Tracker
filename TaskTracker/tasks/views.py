from django.shortcuts import render, redirect,get_object_or_404
from .models import Task
from .forms import TaskForm
from django.views.decorators.http import require_POST
from django.utils import timezone

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def completed_tasks(request):
    tasks = Task.objects.filter(status='done')
    return render(request, 'tasks/completed_tasks.html', {'tasks': tasks})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/update_task.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

def ongoing_tasks(request):
    tasks = Task.objects.exclude(status='done')
    return render(request, 'tasks/ongoing_tasks.html', {'tasks': tasks})

@require_POST
def complete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.status = 'done'  # STATUS_CHOICES içindeki uygun değer= models.DateTimeField(null=True, blank=True)
    task.completed_at=timezone.now()
    task.save()
    return redirect('task_list')
