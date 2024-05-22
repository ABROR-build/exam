from django.db import models
from django.contrib.auth.models import AbstractUser


class Accounts(AbstractUser):
    age = models.IntegerField(default=18)
    bio = models.CharField(max_length=1000, null=True, blank=True)
    seller = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'Accounts'

    def __str__(self):
        return self.username
