from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Авторизация пользователя
    """
    username = None
    email = models.EmailField(unique=True, verbose_name="электронный адрес")

    avatar = models.ImageField(upload_to="users/", verbose_name="аватар")
    phone = models.CharField(max_length=35, verbose_name="номер телефона")
    country = models.CharField(max_length=50, verbose_name="страна")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
