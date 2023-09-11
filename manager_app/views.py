from django.shortcuts import render
from .models import Player


def home(request):
    return render(request, 'manager_app/home.html')
