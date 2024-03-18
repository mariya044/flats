from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    fio=models.CharField(max_length=255,default="")
    birth_date=models.DateField(default="2000-01-12")





# Create your models here.
