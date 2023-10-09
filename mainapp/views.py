from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html')


def about(request):
    return render(request, 'mainapp/about.html')


def user_register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            messages.success(request, 'Te has registrado correctamente !!')
            form.save()
            return redirect('index')

    return render(request, 'mainapp/register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido {user}!!')
            return redirect('index')
        else:
            messages.warning(
                request, 'No te has identificado correctamente !!')

    return render(request, 'mainapp/login.html')


def user_logout(request):
    logout(request)
    return redirect('user_login')
