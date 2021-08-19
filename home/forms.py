from django import forms


class LinkAddForm(forms.Form):
    title = forms.CharField(max_length=64)
    url = forms.CharField()

    def clean_title(self):
        title = self.cleaned_data.get("title")
        return title.strip()

    def clean_url(self):
        url = self.cleaned_data.get("url")
        return url.strip()