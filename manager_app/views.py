from django.shortcuts import render
from .models import Player


def index(request):
    return render(request, 'manager_app/template.html')
