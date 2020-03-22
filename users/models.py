from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class CustomUser(AbstractUser):
    patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    zip_code = models.CharField(max_length=10,null=True)
    number_of_flatmates = models.IntegerField(null=True)
