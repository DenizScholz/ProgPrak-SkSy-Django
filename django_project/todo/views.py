from django.shortcuts import render, HttpResponse
from .models import Todo

# Create your views here.
def home(request):
    context = {
        'title': 'Home',
        'todos': Todo.objects.all(),
    }
    return render(request, 'todo/home.html', context)

def impressum(request):
    context = {
        'title': 'Impressum',
    }
    return render(request, 'todo/impressum.html', context)
