from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .helper import *
from .models import *

# Create your views here.
contents = []


@login_required(login_url='login')
def home(request):
    db_obj = PromptData.objects.filter(userid=request.user)

    if request.method == 'POST':
        prompt = request.POST.get('prompt')

        response = find_similarity(prompt)

        try:
            link = image(prompt)
        except:
            link = ""

        if response == []:
            response = chatGPT(prompt)
        else:
            response = response[0][1]

        PromptData.objects.create(
            userid=request.user, prompt=prompt, output=response, img=link).save()

        return HttpResponseRedirect(reverse('chatbot-home'))

    return render(request, 'base.html', context={'data': reversed(db_obj)})


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

                db_obj = PromptData.objects.create(userid=request.user)
                db_obj.save()

                return redirect('home')

            except:
                print("Error")

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')
