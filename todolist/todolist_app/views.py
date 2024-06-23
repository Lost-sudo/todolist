from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUser, TaskForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Tasks

# Create your views here.

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username oor password is incorrect.")
    return render(request, 'todolist_app/login.html')

def signup_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = CreateUser(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, "Account was created for " + username)
                return redirect('login')
        else:
            form = CreateUser
    
    context = {'form':form}
    return render(request, 'todolist_app/signup.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def homepage(request):
    user_task = Tasks.objects.filter(user=request.user)
    return render(request, 'todolist_app/home.html', {'tasks': user_task})

@login_required(login_url='login')
def add_task(request):
    if request.method == 'POST':
        taskform = TaskForm(request.POST)
        if taskform.is_valid():
            task = taskform.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
    else:
        taskform = TaskForm()

    context = {'taskform':taskform}
    return render(request, 'todolist_app/add_task.html', context)

@login_required(login_url='login')
def toggle_task_status(request, task_id):
    task = get_object_or_404(Tasks, id=task_id, user=request.user)
    if task.status == 'C':
        task.status = 'P'
    else:
        task.status = 'C'
    task.save()
    return redirect('home')