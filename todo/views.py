from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/index.html', context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')

def editTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'task': task}
    return render(request, 'todo/edit.html', context)


def toggleComplete(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = not task.completed
    task.save()
    return redirect('/')

def home(request):
    return render(request, 'home.html')