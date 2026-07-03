from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom Schema (Used in AUTH_USER_MODEL)
class OrainAuth(AbstractUser):
    cash = models.IntegerField(default=0, null=True)

    # For Django admins
    def __str__(self) -> str:
        return self.username