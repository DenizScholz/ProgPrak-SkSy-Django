"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
from todo import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo/new/', views.todo_new, name='todo_new'),
    path('todo/delete/<int:id>/', views.todo_delete, name='todo_delete'),
    path('todo/<int:id>/', views.todo_detail, name='todo_detail'),
    path('todo/<int:id>/edit/', views.todo_edit, name='todo_edit'),
    path('impressum/', views.impressum, name='impressum'),
]
