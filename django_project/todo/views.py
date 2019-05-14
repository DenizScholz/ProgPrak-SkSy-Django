from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Todo
from datetime import datetime
from .forms import TodoForm

def home(request):
    context = {
        'title': 'Home',
        'todos': Todo.objects.all(),
    }
    return render(request, 'todo/home.html', context)

def todo_new(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('home')
    else:
        form = TodoForm()
    context = {
        'form': form,
        'title': 'New Todo',
    }
    return render(request, 'todo/todo_edit.html', context)

def todo_edit(request, id):
    todo = get_object_or_404(Todo, pk=id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_detail', id=todo.pk)
    else:
        form = TodoForm(instance=todo)
    context = {
        'form': form,
        'title': 'Edit Todo',
    }
    return render(request, 'todo/todo_edit.html', context)

def todo_delete(request, id):
    todo = get_object_or_404(Todo, pk=id)
    todo.delete()
    return redirect('home')

def todo_detail(request, id):
    todo = get_object_or_404(Todo, pk=id)
    context = {
        'title': 'Impressum',
        'todo': todo,
    }
    return render(request, 'todo/todo_detail.html', context)

def impressum(request):
    context = {
        'title': 'Impressum',
    }
    return render(request, 'todo/impressum.html', context)
