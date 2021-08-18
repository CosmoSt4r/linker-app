from django import forms
from django.core.exceptions import ValidationError
from .models import Link
from django.contrib.auth import authenticate


class LinkAddForm(forms.Form):
    title = forms.CharField(max_length=64)
    url = forms.CharField()
