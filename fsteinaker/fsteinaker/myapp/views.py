from django.http import HttpResponse, JsonResponse
from .models import Trabajo, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def trabajo(request):
    trabajo = Trabajo.objects.all()
    return render(request, 'trabajo.html',{
        'trabajos':trabajo
    } )

def task(request):
    tasks = Task.objects.all()
    return render(request, 'task.html', {
        'tasks': tasks
    })