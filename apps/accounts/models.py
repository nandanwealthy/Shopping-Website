from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User model.
    Inherits all fields and behavior from Django's AbstractUser.
    We'll extend this model in future lessons.
    """

    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username