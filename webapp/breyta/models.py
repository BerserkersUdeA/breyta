from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bitcoin = models.CharField(max_length=256, blank=True)
    xrp = models.CharField(max_length=256, blank=True)
    ethereum = models.CharField(max_length=256, blank=True)
    litecoin = models.CharField(max_length=256, blank=True)


def __str__(self):
    return self.user.username
