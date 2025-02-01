from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class MYUSERS(AbstractUser):
    Phonenumber=models.IntegerField
    Age=models.IntegerField
