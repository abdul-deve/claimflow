from django.contrib import admin
from user.models import (User,
                         Roles, UserRole,
                         )
# Register your models here.
admin.site.register(User)
admin.site.register(Roles)
admin.site.register(UserRole)

