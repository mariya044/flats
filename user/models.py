from django.db import models



class Customer(models.Model):
    name=models.CharField(max_length=30,blank=True, null=True)
    password=models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Seller(models.Model):
    company_name=models.CharField(max_length=30,blank=True, null=True)
    password=models.CharField(max_length=40)

    def __str__(self):
        return self.company_name


# Create your models here.
