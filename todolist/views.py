from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Task, Tag

def home(request):
    tasks = Task.objects.all()
    return render(request, 'todolist/home.html', {'tasks': tasks})

def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.toggle_status()
    return redirect('home')


class TagListView(ListView):
    model = Tag
    template_name = 'todolist/tag_list.html'
    context_object_name = 'tags'
