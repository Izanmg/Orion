from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to="profiles/",blank=True,null=True,default="/profiles/default_profile_picture.jpg")