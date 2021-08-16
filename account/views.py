from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':

        form = SignupForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            User.objects.create_user(username=username, password=password)
            
            # return redirect('account:home')
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})
