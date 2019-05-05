from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'todo/home.html', context)