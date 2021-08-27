from django.http.response import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SearchUserForm
from django.contrib.auth.models import User
from home.models import QRCode


def main_view(request):
    if request.method == "POST":

        form = SearchUserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            return redirect(reverse("main-page:show-user", args=[username]))
    else:
        form = SearchUserForm()

    return render(request, "main.html", {"form": form})


def show_user(request, username):
    try:
        user = User.objects.filter(username=username).get()
    except User.DoesNotExist:
        raise Http404("User does not exist")

    codes = QRCode.objects.filter(user=user)
    return render(
        request, "user.html", context={"user": user, "codes": codes}
    )
