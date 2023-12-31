from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm, AddPlayerForm
from .models import Player


def home(request):
    current_user = request.user
    players = Player.objects.filter(user=current_user.id)
    context = {
        'menu_item': 'home',
        'players': players,
    }

    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in.')
            return redirect('home')
        else:
            messages.success(
                request, 'There was an error logging in. Please try again.')
            return redirect('home')
    else:
        return render(request, 'manager_app/home.html', context)


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


def register_user(request):
    context = {
        'menu_item': 'register',
    }

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, 'You have successfully registered. Welcome!')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'manager_app/register.html', {**context, 'form': form})


def view_player(request, pk):
    if request.user.is_authenticated:
        player = Player.objects.get(id=pk)
        return render(request, 'manager_app/view.html', {'player': player})
    else:
        messages.success(
            request, 'You must be logged in to view player information.')
        return redirect('home')


def delete_player(request, pk):
    if request.user.is_authenticated:
        deleted = Player.objects.get(id=pk)
        deleted.delete()
        messages.success(request, 'Player deleted successfully')
        return redirect('home')
    else:
        messages.success(request, 'You must be logged in to delete a player.')
        return redirect('home')


def add_player(request):
    form = AddPlayerForm(request.POST or None)
    context = {
        'menu_item': 'add_player',
        'form': form,
    }

    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_player = form.save(commit=False)
                add_player.user = User.objects.get(pk=request.user.id)
                add_player.save()
                messages.success(request, 'Player added successfully')
                return redirect('home')
        return render(request, 'manager_app/add.html', context)
    else:
        messages.success(request, 'You must be logged in to add players.')
        return redirect('home')


def update_player(request, pk):
    player = Player.objects.get(id=pk)
    form = AddPlayerForm(request.POST or None, instance=player)
    context = {
        'player': player,
        'form': form,
    }

    if request.user.is_authenticated:
        if form.is_valid():
            form.save()
            messages.success(request, 'Player has been updated.')
            return redirect('home')
        return render(request, 'manager_app/update.html', context)
    else:
        messages.success(request, 'You must be logged in to update players.')
