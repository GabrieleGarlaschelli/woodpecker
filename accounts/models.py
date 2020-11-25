from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    def __str__(self):
        return self.email

class Customer(models.Model):
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  birthday = models.DateField(null=True)

  def __str__(self):
    return "%s" % self.user

class Address(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  address = models.TextField(null=False)
  city = models.CharField(max_length=255)
  postal_code = models.CharField(max_length=20)
  county = models.CharField(max_length=20)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

  def __str__(self):
    return "%s, " % self.customer + "%s" % self.address

