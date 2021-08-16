from django.contrib.auth.models import User
from django.contrib import messages

def check_username(request, username):
    if User.objects.filter(username=username).exists():
        messages.info(request, "Username already exists")
    if not 8 <= len(username) <= 32:
        messages.info(request, "Username must be from 8 to 32 characters long")

def check_password(request, password, confirm_password):
    if password != confirm_password:
        messages.info(request, "Passwords aren't matching")
    if len(password) < 8:
        messages.info(request, "Password must contain at least 8 characters")
