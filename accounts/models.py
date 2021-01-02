from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  liked_woodworks = models.ManyToManyField(to="woodworks.Woodwork", through="woodworks.Like")

  def __str__(self):
      return self.email

class Customer(models.Model):
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  birthday = models.DateField(null=True)

  def __str__(self):
    return "%s" % self.user
  
  def fullname(self):
    return "%s %s" % (self.user.first_name, self.user.last_name)

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

class Chat(models.Model): 
  OPENED = 'opened'
  CLOSED = 'closed'

  STATUSES = [
    (OPENED, 'Aperta'),
    (CLOSED, 'Chiusa')
  ]

  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  status = models.CharField(max_length=255, choices=STATUSES, default=OPENED)
  created_at = models.DateTimeField()

  class Meta:
    db_table = "chats"

class Message(models.Model):
  chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
  body = models.TextField(null=False)
  sender = models.CharField(max_length=255)
  created_at = models.DateTimeField()

  class Meta:
    db_table = "messages"

