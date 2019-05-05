from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'todo/home.html', context)

def impressum(request):
    context = {
        'title': 'Impressum',
    }
    return render(request, 'todo/impressum.html', context)
