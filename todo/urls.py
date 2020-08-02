from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.home, name='home'),
    path('new_task/', views.new_task, name='new_task'),
    path('delete_task/<int:todo_id>', views.delete_task, name='delete_task')
]
