from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import QRCode
from django.contrib.auth.models import User
from .forms import QRCodeAddForm


@login_required(login_url="account:login")
def edit_code_view(request, id):
    code = get_object_or_404(QRCode, id=id)
    if code.user != request.user:
        raise Http404("Code not found")

    if request.method == "POST":

        if request.POST.get("submit"):
            form = QRCodeAddForm(request.POST)

            if form.is_valid():
                code.title = form.cleaned_data.get("title")
                code.text = form.cleaned_data.get("text")
                code.save()

        return redirect("account:home:edit")
    else:
        form = QRCodeAddForm()
        form.initial = {"title": code.title, "text": code.text}

    return render(request, "edit_code.html", {"code": code, "form": form})


@login_required(login_url="account:login")
def delete_code_view(request, id):
    code = get_object_or_404(QRCode, id=id)
    if code.user != request.user:
        raise Http404("QRCode not found")

    if request.method == "POST":
        if request.POST.get('delete'):
            QRCode.objects.filter(id=code.id).delete()
        return redirect("account:home:edit")

    return render(request, "delete.html", {"code": code})


@login_required(login_url="account:login")
def add_code_view(request):
    if request.method == "POST":

        form = QRCodeAddForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']

            QRCode.objects.create(user=request.user, title=title, text=text)
            
            return redirect("qrcode:add")
    else:
        form = QRCodeAddForm()

    return render(request, "add.html", {"form": form})


def show_code_view(request, id):
    code = get_object_or_404(QRCode, id=id)
    source = f'https://image-charts.com/chart?chs=200x200&cht=qr&chl={code.text}&choe=UTF-8'
    return render(request, "show.html", {"code": code, "code_source" : source})


def show_user_view(request, username):
    user = get_object_or_404(User, username=username)
    user = {'username' : user.username, 'links_count' : QRCode.objects.filter(user=user).count()}
    source = f'https://image-charts.com/chart?chs=200x200&cht=qr&chl={request.META["HTTP_HOST"] + "/" + username}&choe=UTF-8'
    return render(request, "user_code.html", {"user": user, "code_source" : source})
