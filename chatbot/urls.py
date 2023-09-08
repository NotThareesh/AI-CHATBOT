from django.urls import path

from chatbot.views import *

urlpatterns = [
    path('login', login_and_regsiter_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('', home, name='home'),
    # path('speak', speak_text, name='speak-text')
]
