from django.shortcuts import render, redirect
from .models import Link
from .forms import LinkAddForm


def main_view(request):
    if not request.user.is_authenticated:
        return redirect("account:login")

    links = Link.objects.filter(user=request.user)
    return render(request, "home.html", {"user": request.user, "links": links})


def add_link_view(request):
    if not request.user.is_authenticated:
        return redirect("account:login")

    if request.method == "POST":

        form = LinkAddForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get("title")
            url = form.cleaned_data.get("url")

            Link.objects.create(user=request.user, title=title, url=url)

            return redirect("account:home:add-link")
    else:
        form = LinkAddForm()

    return render(request, "add_link.html", {"form": form})


def edit_link_view(request, id):
    link = Link.objects.get(id=id)
    return render(request, "home.html", {"link": link})
