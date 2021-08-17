from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    url = models.TextField()

    def get_absolute_url(self):
        return reverse("account:home:edit", kwargs={'id' : self.id})