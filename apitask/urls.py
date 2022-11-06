from django.urls import path
from apitask import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('task/', views.getTasks, name="tasks"),
    # path('task/create/', views.createNote, name="create-task"),
    #path('task/<str:pk>/update/', views.updateNote, name="update-task"),
    #path('task/<str:pk>/delete/', views.deleteNote, name="delete-task"),

    path('task/<str:pk>/', views.getTask, name="task"),
]