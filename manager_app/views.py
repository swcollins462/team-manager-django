from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


def home(request):
    context = {
        'menu_item': 'home',
    }

    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in!')
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
        'page': 'Register',
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

    return render(request, 'manager_app/register.html', {**context, 'form': form})
