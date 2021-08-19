from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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


def edit_view(request):
    if not request.user.is_authenticated:
        return redirect("account:login")

    links = Link.objects.filter(user=request.user)

    return render(request, "edit.html", {"user": request.user, "links": links})


def edit_link_view(request, id):
    if not request.user.is_authenticated:
        return redirect("account:login")

    link = get_object_or_404(Link, id=id)
    if link.user != request.user:
        return HttpResponse(404)

    if request.method == "POST":

        form = LinkAddForm(request.POST)

        if form.is_valid():
            link.title = form.cleaned_data.get('title')
            link.url = form.cleaned_data.get('url')
            link.save()
            return redirect("account:home:main")
    else:
        form = LinkAddForm()
        form.initial = {'title' : link.title, 'url' : link.url}

    return render(request, "edit_link.html", {"link" : link, "form" : form})
