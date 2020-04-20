from django.urls import path
from .Login.Controller import *

urlpatterns = [
    path('Login', Login.login),
]