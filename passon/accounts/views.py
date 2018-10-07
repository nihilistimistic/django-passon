from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

from .forms import SignUpForm

# Create your views here.


def login_view(request):
    # implement next in login!!!
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # redirect to home
            return redirect('home:home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def signup_view(request):
    # implement next in signup!!!
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.reg = form.cleaned_data.get('reg')
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.phone_num = form.cleaned_data.get('phone_num')
            user.profile.address = form.cleaned_data.get('address')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
                # redirect to home
                return redirect('home:home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
