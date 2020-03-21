from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    gender = models.IntegerField(choices=(("1","male"),("2","female"),("3","divers")))
    zip_code = models.CharField(max_length=10,null=True)
    number_of_flatmates = models.IntegerField(null=True)
