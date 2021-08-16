from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profileIMG = models.ImageField(upload_to="static/users/images", blank=True)
    backgroundIMG = models.ImageField(upload_to="static/users/images", blank=True)
    websiteURL = models.URLField(blank=True)

    objects = models.Manager()
