from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from . import utils

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        utils.check_username(request, username)
        utils.check_password(request, password, confirm_password)

        if len(messages.get_messages(request)) == 0:
            User.objects.create_user(username=username, password=password)
            return redirect('account:home')
        else:
            return render(request, "signup.html", {"username" : username})
    else:
        return render(request, "signup.html", {})
