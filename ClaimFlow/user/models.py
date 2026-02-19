from django.db import models
from utils.models import TimeStamp
from django.contrib.auth.models import AbstractUser
from user.manager import UserManager



class User(AbstractUser,TimeStamp):
    email = models.EmailField(unique=True, db_index=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return f"ID:{self.id}email : {self.email}"



class Roles(TimeStamp):
    roles_choices = [
        ('admin','Administrator'),
        ('manager','Manager'),
        ('patient','Patient')
    ]
    role = models.CharField(max_length=25,choices=roles_choices,unique=True)

    def __str__(self):
        return self.role

class UserRole(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_roles")
    role = models.ForeignKey(Roles,on_delete=models.CASCADE,related_name="roles")




