from django.db import models
from django.contrib.auth import get_user_model

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseModel(TimeStamp):
    pass

# class Device(TimeStamp):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_device")
#     attempts = models.PositiveSmallIntegerField(default=0)
#     max_attempts = models.PositiveSmallIntegerField(default=3)
#     secret_key = models.CharField(max_length=16)
#     last_failed_attempt = models.DateTimeField(null=True, blank=True)
#
#     def is_valid(self) -> bool:
#         return self.attempts < self.max_attempts
#
#     def reset(self):
#         self.attempts = 0
#         self.last_failed_attempt = None
#         self.save(update_fields=["attempts", "last_failed_attempt"])
#         return self
