from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todo_list.html', {'todos': todos})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'add_task.html', {'form': form})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id, user=request.user)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=task)

    return render(request, 'edit_task.html', {'form': form, 'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id, user=request.user)
    task.delete()
    return redirect('todo_list')
