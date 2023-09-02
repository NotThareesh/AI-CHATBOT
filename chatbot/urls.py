from django.urls import path

from chatbot.views import *

urlpatterns = [
    path('', home, name='home'),
    # path('api', chatAPI, name='chatAPI')
]