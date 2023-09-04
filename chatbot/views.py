from django.shortcuts import render, HttpResponse
from .models import PromptData
from .helper import *
import random

greetings = (
  "Hello!",
  "Hi there!",
  "Greetings!",
  "Hey!",
  "Welcome!",
  "Good day!",
  "Nice to see you!",
  "How's it going?",
  "Great to have you here!"
)

contents = []

# Create your views here.
def home(request):
    if request.method == 'POST':
        data = request.POST.get('prompt')

        response = chatGPT(data)

        contents.append([data, response])

        instance = PromptData.objects.create(
            username='None',
            prompt=contents,
        )

        instance.save()

    greeting = random.choice(greetings)

    return render(request, 'base.html', context={'data': contents, 'user': 'None', 'greeting': greeting})


def login_page(request):
    return render(request, 'login.html')
