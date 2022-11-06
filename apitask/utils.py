from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


def getTasklist(request):
    task = Task.objects.all().order_by('-updated_at')
    serializer = TaskSerializer(task, many=True)
    return Response (serializer.data)

def getTaskId (request, pk):
    task = Task.objects.get (id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response (serializer.data)

def createTask(request):
    data = request.data
    task = Task.objects.create(
        title = data['title'],
        description= data['description']
    )
    serializer = TaskSerializer(task, many=False) 
    return Response (serializer.data)

def updateTask(request, pk):
    data = request.data
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=data)

    if serializer.is_valid():
        serializer.save()
    return Response (serializer.data)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Note was deleted!')