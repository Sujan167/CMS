from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'App/index.html')


def loginpage(request):
    form = UserForm()
    if request.method == 'POST':
        username = request.POST['usernmae']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            form = UserForm()
    context = {'form': form}
    return render(request, 'App/login.html', context)
