from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .helper import *

contents = []

# Create your views here.


def home(request):
    if request.method == 'POST':
        data = request.POST.get('prompt')

        response = find_similarity(data)

        if response == []:
            response = chatGPT(data)
            contents.append([data, response])
        else:
            contents.append([data, response[0][1]])

    return render(request, 'base.html', context={'data': contents[::-1]})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password)

        try:
            User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print('Login Done')
            return redirect('home')
        else:
            messages.error(request, "Username or Password is incorrect")

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def register_user(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)

            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {'form': form}

    return render(request, 'login.html', context=context)
