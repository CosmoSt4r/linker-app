from django import forms
from .models import QRCode


class QRCodeAddForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Your title'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'cols' : 80, 'rows' : 10, 'class' : 'form-control', 'placeholder' : 'Your text or URL'}))

class LinkAddForm:
    ...

