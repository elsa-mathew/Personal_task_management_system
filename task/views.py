from django.shortcuts import redirect, render
import datetime
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from datetime import date

def task_detail(request, task_id):
    
    task = None  
    if request.method == 'GET':
        task = Task.objects.get(id=task_id)
        
    return render(request, 'task_detail.html', {'task': task})

@login_required
def create_task(request):
    
    if request.method == 'POST':
        
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')
        file = request.FILES.get('file')
        status = request.POST.get('status')

        
        task = Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            priority=priority,
            due_date=due_date,
            file=file,
            status=status,
        )

        messages.success(request, "Task created successfully.")
        return redirect("view_task", id=task.id)

    return render(request, 'task_create.html')




@login_required
def my_tasks(request):

    tasks = Task.objects.filter(
    user=request.user
).order_by("-created_at")

    for task in tasks:
        if task.due_date < date.today() and task.status != 'Completed':
            task.is_overdue = True
        else:
            task.is_overdue = False

    search = request.GET.get("search")

    if search:
        tasks = tasks.filter(title__icontains=search)

    status = request.GET.get("status")

    if status:
        tasks = tasks.filter(status=status)

    priority = request.GET.get("priority")

    if priority:
        tasks = tasks.filter(priority__iexact=priority)

    sort = request.GET.get("sort")

    if sort == "newest":
        tasks = tasks.order_by("-created_at")

    elif sort == "oldest":
        tasks = tasks.order_by("created_at")

    elif sort == "due_date":
        tasks = tasks.order_by("due_date")

    elif sort == "priority":

        priority_order = {
            "High": 1,
            "Medium": 2,
            "Low": 3,
        }

        tasks = sorted(
            tasks,
            key=lambda x: priority_order.get(x.priority, 4)
        )

    else:
        tasks = tasks.order_by("-created_at")

    paginator = Paginator(tasks, 10)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    for task in page_obj:
        if task.due_date < date.today() and task.status != 'Completed':
            task.is_overdue = True
        else:
            task.is_overdue = False

    context = {

        "page_obj": page_obj,

    }

    return render(request, "my_tasks.html", context)

@login_required
def task_delete(request, task_id):
    
    task = None  
    if request.method == 'POST':
        
        task = Task.objects.get(id=task_id)
        task.delete()


    return render(request, 'task_delete.html', {'task': task})

def task_complete(request, task_id):
    
    task = None  
    if request.method == 'POST':

        task = Task.objects.get(id=task_id)
        task.status = 'Completed'
        task.save()
    return render(request, 'task_complete.html', {'task': task})

def task_incomplete(request, task_id):
    
    task = None  
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        task.status = 'Not Started'
        task.save()
    return render(request, 'task_incomplete.html', {'task': task})


def task_search(request):
    
    query = request.GET.get('q', '')  
    tasks = []  

    return render(request, 'task_search.html', {'tasks': tasks, 'query': query})

def task_filter(request):
    
    filter_criteria = request.GET.get('filter', '')  
    tasks = []  


    return render(request, 'task_filter.html', {'tasks': tasks, 'filter_criteria': filter_criteria})

def task_sort(request):
    
    sort_criteria = request.GET.get('sort', '') 
    tasks = []  

    return render(request, 'task_sort.html', {'tasks': tasks, 'sort_criteria': sort_criteria})



@login_required
def view_task(request, id):

    task = get_object_or_404(

    Task,

    id=id,

    user=request.user

)

    context = {
        'task': task
    }

    return render(request, 'view_task.html', context)


@login_required
def update_task(request, id):

    task = get_object_or_404(

    Task,

    id=id,

    user=request.user

)

    if request.method == "POST":

        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.priority = request.POST.get("priority")
        task.status = request.POST.get("status")
        task.due_date = request.POST.get("due_date")

        if request.FILES.get("file"):
            task.file = request.FILES.get("file")

        task.save()

        messages.success(request, "Task updated successfully!")

        return redirect("my_tasks")


@login_required
def delete_task(request, id):

    task = get_object_or_404(

    Task,

    id=id,

    user=request.user

)

    if request.method == "POST":

        task.delete()

        messages.success(request, "Task deleted successfully.")

        return redirect("my_tasks")

    return redirect("my_tasks")