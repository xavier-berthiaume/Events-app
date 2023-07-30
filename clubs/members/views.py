from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import RegisterUserForm

# Create your views here.
def login_user(request):
    context = {}

    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request=request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.success(request, "There was an error logging in, try again")
            return redirect('login-user')

    else:
        return render(request, 'authentication/login.html', context)


def logout_user(request):
    context = {}
    logout(request)
    messages.success(request, "You are now logged out")
    return redirect('home')


def register_user(request):
    context = {

    }

    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect('home')

    else:
        context['form'] = RegisterUserForm()

    return render(request, 'authentication/register_user.html', context)
