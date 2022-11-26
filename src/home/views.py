from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterUserForm
from api.views import dashboard_data_main,dashboard_data

def index(request):
    return render(request, 'index.html', {})

@login_required(login_url='/login/')
def dashboard(request):
    if request.user.is_authenticated:
        username = str(request.user)
        data = dashboard_data_main(username)
        data2 = dashboard_data(username)
        data2.append(data)
        return render(request, 'dashboard.html', {'data':data,'data2':data2})

@login_required(login_url='/login/')
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', )

@login_required()
def upload(request):
    return render(request, 'upload.html', {})

def page_404(request):
    return render(request, 'page_404.html', {})

@login_required(login_url='/login/')
def resume(request,file_id):
    print(file_id)
    return render(request, 'resume.html', {})

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.success(request, ("There Was An Error Logging In, Try Again..."))	
                return redirect('login')	

        else:
            return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out!"))
    return redirect('index')


def register_user(request):
    #print(request.user.is_authenticated())
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            form = RegisterUserForm(request.POST)
            context ={}
            context['form']= form
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, ("Registration Successful!"))
                return redirect('home')
        else:
            form = RegisterUserForm()

        return render(request, 'auth/register_user.html', {
            'form':form,
            })