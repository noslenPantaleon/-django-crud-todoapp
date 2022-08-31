from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task
from django.urls import reverse
from .forms import TaskForm
# Create your views here.


def list_tasks(request):
    tasks = Task.objects.all()
    context = {
        'tasks':tasks,
        'update': None
    }
    return render(request, 'index.html', context)


def create_task(request):
    try:
        task_title= request.POST['title']
        task_description= request.POST['description']
        if task_title == "" or task_description == "":
            raise ValueError ("the text field can not be empty")
        task_db = Task(title= task_title,
                    description=task_description)
        task_db.save()
        return redirect('/tasks/')
     
    except ValueError as err:
        print (err)
        return redirect('/tasks/')
        #return HttpResponseRedirect(reverse('list_tasks'))




def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')
    #return HttpResponseRedirect(reverse('tasks'))

def update(request):
    task_id = request.POST.get("id")
    task_title= request.POST.get("title")
    task_description = request.POST.get("description")
    if request.method =="POST":
        db_data = Task.objects.get(id=task_id)
        db_data.title = task_title
        db_data.description = task_description
        print("updating")
        db_data.save()
        context= {"task_title":   db_data.title,
        "task_description":   db_data.description}
        return redirect('/tasks/')
    
    return render(request,  'index.html', context)
         
    # return HttpResponseRedirect(reverse("list_tasks"))     



def edit(request, task_id):
    db_data = Task.objects.all()
    db_data_only = Task.objects.get(id=task_id)
    print(db_data_only)
    context = {
        "db_data": db_data[::-1],
        "update": db_data_only
    }
    print (context)

    return render(request,  'index.html', context)
 



# def create_task(request):
#     form = TaskForm()
#     if request.method == "POST":
#         form=TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/tasks/')
#         context ={"form": form}
#         return render (request, 'new_task.html', context)





