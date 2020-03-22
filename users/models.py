from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class CustomUser(AbstractUser):
    patientId = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    zipCode = models.CharField(max_length=10,null=True)
    numberOfFlatmates = models.IntegerField(null=True)
