from django.db import models


class Contact(models.Model):
    DEAL_CHOICES = (
        ("rent", "rent"),
        ("purchase", "purchase"),
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)
    deal_type = models.CharField(max_length=100, choices=DEAL_CHOICES)

    def __str__(self):
        return self.email
