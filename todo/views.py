from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDo

# Create your views here.


def home(request):

    todos = ToDo.objects.filter()
    todos_for_front = prepare_todos_list(todos)

    context = {
        'todos': todos_for_front,
    }

    return render(request, 'todo/new_task.html', context)


def new_task(request):

    task_text = request.POST.get('task_text')
    is_urgent_response = request.POST.get('is_urgent')

    is_urgent = True if is_urgent_response == 'true' else False

    # Tworze nowy wpis do bazy danych

    if task_text != "":
        todo_object = ToDo(text=task_text, is_urgent=is_urgent)
        todo_object.save()

    # Pobieram list wpisow z bazy danych i tworze ich liste

    todos = ToDo.objects.filter()
    todos_for_front = prepare_todos_list(todos)

    context = {
        'todos': todos_for_front,
    }
    # Stworzona liste zwracam

    return render(request, 'todo/new_task.html', context)


def delete_task(request):

    # Wyszukuje i usuwam dany wpis

    # Pobieram list wpisw z bazy danych i tworze ich liste

    # Zwracam stworzona liste

    return render(request, 'todo/new_task.html')


def prepare_todos_list(todos):
    todos_for_front = []

    for todo in todos:
        post_text = todo.text
        post_urgent = 'Task is urgent' if todo.is_urgent else 'Task is not urgent'
        todos_for_front.append((post_text, post_urgent))

    return todos_for_front
