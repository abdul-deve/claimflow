from django.db import models
from utils.models import TimeStamp
from django.contrib.auth.models import AbstractUser
from user.manager import UserManager




class User(AbstractUser):
    email = models.EmailField(unique=True, db_index=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = UserManager()



class Roles(TimeStamp):
    roles_choices = [
        ('admin','Administrator'),
        ('manager','Manager'),
        ('patient','Patient')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="roles")
    name = models.CharField(max_length=25,choices=roles_choices)



