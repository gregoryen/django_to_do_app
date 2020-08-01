from django.shortcuts import render
from .models import ToDo

# Create your views here.


def home(request):
    return render(request, template_name='todo/index.html')


def new_task(request):

    # Tworze nowy wpis do bazy danych

    # Pobieram list wpisow z bazy danych i tworze ich liste

    # Stworzona liste zwracam

    return render(request, 'todo/new_task.html')


def delete_task(request):

    # Wyszukuje i usuwam dany wpis

    # Pobieram list wpisw z bazy danych i tworze ich liste

    # Zwracam stworzona liste

    return render(request, 'todo/new_task.html')
