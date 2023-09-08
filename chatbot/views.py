from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .helper import *
from .models import *

contents = []

# Create your views here.


@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        data = request.POST.get('prompt')

        response = find_similarity(data)

        if response == []:
            response = chatGPT(data)
            contents.append([data, response])
        else:
            contents.append([data, response[0][1]])

        # db_obj = PromptData.objects.filter(username=request.user)

        # db_obj.data = str(contents)

        # db_obj.save()

    return render(request, 'base.html', context={'data': contents[::-1], 'user': request.user})


def login_and_regsiter_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if 'login' in request.POST:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                print('Invalid Creds')

        else:
            try:
                user = User.objects.create_user(
                    username=username.lower(), password=password)
                user.save()

                user = authenticate(
                    request, username=username, password=password)
                login(request, user)

                db_obj = PromptData.objects.create(
                    username=request.user,
                )

                db_obj.save()

                return redirect('home')

            except:
                print("Error")

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')
