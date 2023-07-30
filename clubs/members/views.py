from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
