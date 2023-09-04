from django.urls import path

from chatbot.views import *

urlpatterns = [
    path('', home, name='home'),
    path('login', login_page, name='login_page')
]