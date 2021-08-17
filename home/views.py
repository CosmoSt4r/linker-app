from django.shortcuts import render, redirect
from .models import Link


def main_view(request):

    if not request.user.is_authenticated:
        return redirect('account:login')

    return render(request, "home.html", {})


def edit_link_view(request, id):
    link = Link.objects.get(id=id)
    return render(request, "home.html", {'link' : link})
