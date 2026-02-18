from django.db import models
from django.contrib.auth import get_user_model
from utils.models import TimeStamp
User = get_user_model()


class Organization(TimeStamp):
    name = models.CharField(max_length=255,unique=True,db_index=True)
    description = models.TextField()
    admin = models.ForeignKey(User,on_delete=models.CASCADE,related_name="organizations")

    def __str__(self):
        return f"Name: {self.name} Admin: {self.admin}"

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"
        unique_together = ("name", "admin")

class Practice(TimeStamp):
    name = models.CharField(max_length=255,unique=True,db_index=True)
    description = models.TextField()
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE,related_name="practices")
    city = models.CharField(max_length=255)

    def __str__(self):
        return f"Name: {self.name} Organization: {self.organization}"

    class Meta:
        verbose_name = "Practice"
        verbose_name_plural = "Practices"
        unique_together = ("name", "organization")

