from django import forms


class QRCodeAddForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Your title'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'cols' : 80, 'rows' : 10, 'class' : 'form-control', 'placeholder' : 'Your text or URL'}))
    is_link = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={'class' : "form-check-input", 'id' : 'is_link_checkbox'}))
