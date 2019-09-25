from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', null=True, blank=True)
    age = models.PositiveIntegerField(verbose_name='Age', null=True, blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('superadmin:users_detail', args=[str(self.id)])
