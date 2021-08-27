from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import QRCode
from .forms import QRCodeAddForm


@login_required(login_url="account:login")
def main_view(request):
    qrcodes = QRCode.objects.filter(user=request.user)
    return render(request, "home.html", {"user": request.user, "codes": qrcodes})


@login_required(login_url="account:login")
def add_link_view(request):
    if request.method == "POST":

        form = QRCodeAddForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']

            QRCode.objects.create(user=request.user, title=title, text=text)
            
            return redirect("account:home:add-link")
    else:
        form = QRCodeAddForm()

    return render(request, "add_link.html", {"form": form})


@login_required(login_url="account:login")
def edit_view(request):
    codes = QRCode.objects.filter(user=request.user)
    return render(request, "edit.html", {"user": request.user, "codes": codes})


@login_required(login_url="account:login")
def edit_link_view(request, id):
    code = get_object_or_404(QRCode, id=id)
    if code.user != request.user:
        raise Http404("Link not found")

    if request.method == "POST":

        if request.POST.get("submit"):
            form = QRCodeAddForm(request.POST)

            if form.is_valid():
                code.title = form.cleaned_data.get("title")
                code.text = form.cleaned_data.get("text")
                code.save()

        return redirect("account:home:edit-main")
    else:
        form = QRCodeAddForm()
        form.initial = {"title": code.title, "text": code.text}

    return render(request, "edit_link.html", {"code": code, "form": form})


@login_required(login_url="account:login")
def delete_link_view(request, id):
    code = get_object_or_404(QRCode, id=id)
    if code.user != request.user:
        raise Http404("QRCode not found")

    if request.method == "POST":
        if request.POST.get('delete'):
            QRCode.objects.filter(id=code.id).delete()
        return redirect("account:home:edit-main")

    return render(request, "delete_link.html", {"code": code})
