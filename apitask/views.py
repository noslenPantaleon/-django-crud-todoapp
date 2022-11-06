from django.shortcuts import render
from django.http import response
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer
from apitask import serializers
from .utils import getTasklist, getTaskId, createTask, updateTask, deleteTask


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {

        'Endpoint':'/task/',
        'method': 'GET',
        'body': None,
        'description': 'list of task'
        },
           {
            'Endpoint': '/task/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single task object'
        },
        {
            'Endpoint': '/task/create/',
            'method': 'POST',
            'body': {'title': "",
                    'description': ""        
            },
            'description': 'Creates new task'
        },
        {
            'Endpoint': '/task/id/update/',
            'method': 'PUT',
            'body': {'title': "",
                    'description': ""        
            },
            'description': 'update an existing task'
        },
        {
            'Endpoint': '/task/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting task'
        },
    ]

    return Response(routes)


@api_view(['GET', 'POST'])
def getTasks(request):

    if request.method == 'GET':
        return getTasklist(request)

    if request.method == 'POST':
        return createTask(request)


@api_view(['GET', 'PUT', 'DELETE'])
def getTask(request, pk):

    if request.method == 'GET':
        return getTaskId(request, pk)

    if request.method == 'PUT':
        return updateTask(request, pk)

    if request.method == 'DELETE':
        return deleteTask(request, pk)

