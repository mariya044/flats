from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from users.models import CustomUser


class Post(models.Model):
        STATUSES = (
                ("USD","USD"),
                ("BYN", "BYN"),
                ("EUR", "EUR"),
                ("RUB", "RUB")
        )
        title = models.CharField(max_length=250)
        text = models.TextField()
        created_at = models.DateTimeField(default=timezone.now)
        published_at = models.DateTimeField(blank=True, null=True)
        image=models.ImageField(null=False,blank=False,upload_to="images")
        custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

        flor=models.PositiveIntegerField(blank=True, null=True)
        all_floars=models.PositiveIntegerField(blank=True, null=True)
        kitchen_square=models.PositiveIntegerField(blank=True, null=True)
        all_square=models.PositiveIntegerField(blank=True, null=True)
        living_square=models.PositiveIntegerField(blank=True, null=True)
        price=models.IntegerField(blank=True, null=True)
        value= models.CharField(choices=STATUSES, max_length=50, default="USD")
        rooms=models.PositiveIntegerField(blank=True, null=True)
        adress=models.CharField(max_length=250)


        def __str__(self):
            return self.title



# Create your models here.
