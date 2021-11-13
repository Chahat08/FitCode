from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    avatar = models.ImageField(default='../static/img/default.png', upload_to='images/')


