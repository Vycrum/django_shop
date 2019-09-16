from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', null=True, blank=True)
    age = models.PositiveIntegerField(verbose_name='Age', null=True, blank=True)