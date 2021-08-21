from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SearchUserForm(forms.Form):
    username = forms.CharField(min_length=8, max_length=32)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not User.objects.filter(username=username).exists():
            raise ValidationError("Username doesn't exist")
        return username
