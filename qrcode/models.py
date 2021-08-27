from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class QRCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)
    editable = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("qrcode:edit", kwargs={"id": self.id})
