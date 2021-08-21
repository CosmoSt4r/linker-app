from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout


def base_view(request):
    if request.user.is_authenticated:
        return redirect("account:home:main")
    else:
        return redirect("account:login")


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("account:home:main")

    if request.method == "POST":

        form = SignupForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            User.objects.create_user(username=username, password=password)

            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect("account:home:main")
    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("account:home:main")

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("account:home:main")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("account:login")
