from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from task.models import Task
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,"home.html")

def register(request):

    if request.method == "POST":

        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("register")

        user = User.objects.create_user(
            first_name=fullname,
            username=username,
            email=email,
            password=password
        )

        user.save()

        messages.success(request, "Registration Successful.")

        return redirect("login")

    return render(request,"register.html")

def login_page(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            request.session["user_id"] = user.id
            request.session["username"] = user.username
            request.session["full_name"] = user.first_name

            messages.success(request, "Login successful.")

            return redirect("dashboard")

        else:

            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, "login.html")

from datetime import date
from datetime import date
from django.contrib.auth.decorators import login_required
from task.models import Task


@login_required
def dashboard(request):

    tasks = Task.objects.filter(user=request.user)
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
            "high": 1,
            "medium": 2,
            "low": 3,
        }

        tasks = sorted(
            tasks,
            key=lambda x: priority_order.get(x.priority.lower(), 4)
        )

    else:

        tasks = tasks.order_by("-created_at")

    completed_tasks = [
        task for task in tasks
        if task.status == "Completed"
    ]

    inprogress_tasks = [
        task for task in tasks
        if task.status == "In Progress"
    ]

    backlog_tasks = [
        task for task in tasks
        if task.status == "Pending"
    ]

    total_tasks = Task.objects.filter(
        user=request.user
    ).count()

    completed_tasks_count = Task.objects.filter(
        user=request.user,
        status="Completed"
    ).count()

    pending_tasks_count = Task.objects.filter(
        user=request.user,
        status="Pending"
    ).count()

    overdue_tasks_count = Task.objects.filter(
        user=request.user,
        due_date__lt=date.today()
    ).exclude(
        status="Completed"
    ).count()

    upcoming_tasks_count = Task.objects.filter(
        user=request.user,
        due_date__gte=date.today()
    ).exclude(
        status="Completed"
    ).count()

    context = {

        "completed_tasks": completed_tasks,

        "inprogress_tasks": inprogress_tasks,

        "backlog_tasks": backlog_tasks,

        "total_tasks": total_tasks,

        "completed_tasks_count": completed_tasks_count,

        "pending_tasks_count": pending_tasks_count,

        "overdue_tasks_count": overdue_tasks_count,

        "upcoming_tasks_count": upcoming_tasks_count,

    }

    return render(request, "dashboard.html", context)


@login_required
def profile(request):

    user = request.user

    if request.method == "POST":

        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")

        user.save()

        messages.success(request, "Profile updated successfully.")

        return redirect("profile")

    return render(request, "profile.html")



@login_required
def change_password(request):

    if request.method == "POST":

        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password1")
        confirm_password = request.POST.get("new_password2")

        user = request.user

        if not user.check_password(old_password):

            messages.error(request, "Current password is incorrect.")

            return redirect("profile")

        if new_password != confirm_password:

            messages.error(request, "Passwords do not match.")

            return redirect("profile")

        user.set_password(new_password)

        user.save()

        update_session_auth_hash(request, user)

        messages.success(request, "Password updated successfully.")

        return redirect("profile")

    return redirect("profile")

def logout_view(request):

    if request.method == "POST":

        logout(request)

        request.session.flush()

        messages.success(request, "You have been logged out successfully.")

        return redirect("login")

    return render(request, "login.html")
