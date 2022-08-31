from django.urls import path
from .views import create_task, delete_task, list_tasks, update, edit


urlpatterns = [
    path('tasks/', list_tasks, name= 'list_task'),
    path('new_task/', create_task, name='create_task'),
    path('edit/<int:task_id>', edit, name='edit'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('update/', update, name='update')]