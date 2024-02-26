from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task
from .forms import Todo  # Corrected import statement

def members(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        if priority and priority.isdigit():
            task = Task(name=name, priority=int(priority), date=date)
            task.save()
    return render(request, 'index.html', {'task1': task1})

def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')

def update(request, id):
    task = Task.objects.get(id=id)
    f = Todo(request.POST or None, instance=task)  # Corrected form class name
    if f.is_valid():
        f.save()
        return redirect('/')  # Redirect to home page after update
    return render(request, 'edit.html', {'f': f, 'task': task})  # Corrected template name
