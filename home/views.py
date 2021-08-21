from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Link
from .forms import LinkAddForm


@login_required(login_url="account:login")
def main_view(request):
    links = Link.objects.filter(user=request.user)
    return render(request, "home.html", {"user": request.user, "links": links})


@login_required(login_url="account:login")
def add_link_view(request):
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


@login_required(login_url="account:login")
def edit_view(request):
    links = Link.objects.filter(user=request.user)
    return render(request, "edit.html", {"user": request.user, "links": links})


@login_required(login_url="account:login")
def edit_link_view(request, id):
    link = get_object_or_404(Link, id=id)
    if link.user != request.user:
        raise Http404("Link not found")

    if request.method == "POST":

        if request.POST.get("submit"):
            form = LinkAddForm(request.POST)

            if form.is_valid():
                link.title = form.cleaned_data.get("title")
                link.url = form.cleaned_data.get("url")
                link.save()

        return redirect("account:home:edit-main")
    else:
        form = LinkAddForm()
        form.initial = {"title": link.title, "url": link.url}

    return render(request, "edit_link.html", {"link": link, "form": form})


@login_required(login_url="account:login")
def delete_link_view(request, id):
    link = get_object_or_404(Link, id=id)
    if link.user != request.user:
        raise Http404("Link not found")

    if request.method == "POST":
        if request.POST.get('delete'):
            Link.objects.filter(id=link.id).delete()
        return redirect("account:home:edit-main")

    return render(request, "delete_link.html", {"link": link})
