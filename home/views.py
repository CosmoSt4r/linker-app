from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from qrcode.models import QRCode


@login_required(login_url="account:login")
def main_view(request):
    qrcodes = QRCode.objects.filter(user=request.user)
    return render(request, "home.html", {"user": request.user, "codes": qrcodes})


@login_required(login_url="account:login")
def edit_view(request):
    codes = QRCode.objects.filter(user=request.user)
    return render(request, "edit.html", {"user": request.user, "codes": codes})
