from django.db import models
from accounts.models import CustomUser, Customer, Address

class Woodwork(models.Model):
  title = models.TextField()
  description = models.TextField()
  publication_date = models.DateTimeField()
  created_at = models.DateTimeField()
  main_image = models.FileField(upload_to='woodworks/static/woodworks_image', null=True)

  class Meta:
    db_table = "woodworks"

  def __str__(self):
    return self.title + " - " + self.description

  def _short_description(self):
    return self.description[0:200]
  
  def is_liked(self, user):
    return Like.objects.filter(user__id=user.id, woodwork__id=self.id).count() > 0
  
  short_description = property(_short_description)

class Like(models.Model):
  woodwork = models.ForeignKey(Woodwork, on_delete=models.CASCADE)
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  added_at = models.DateTimeField()

  class Meta:
    db_table = "likes"

  def __str__(self):
    return "%s - %s" % (self.user, self.woodwork)


class Order(models.Model):
  RECEIVED = 'received'
  CONFIRMED = 'confirmed'
  PENDING = 'pending'
  DONE = 'done'
  DELIVERED = 'delivered'

  STATUSES = [
    (RECEIVED, 'Ricevuto'),
    (CONFIRMED, 'Confermato'),
    (PENDING, 'Lavoro in corso'),
    (DONE, 'Fatto, in attesa di consegna'),
    (DELIVERED, 'Consegnato'),
  ]

  # il woodwork può essere nullo nel caso di ordini custom
  woodwork = models.ForeignKey(Woodwork, on_delete=models.CASCADE, null=True, blank=True)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  to_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
  order_at = models.DateTimeField()
  status = models.TextField(
    max_length=255,
    choices=STATUSES,
    default=RECEIVED
  )
  notes = models.TextField(null=True, blank=True)
  quantity = models.IntegerField(default=1)
  expiration_on = models.DateTimeField(null=True, blank=True)

  def __str__(self):
    return "%s - %s" % (self.customer, self.woodwork)

class Rating(models.Model):
  woodwork = models.ForeignKey(Woodwork, on_delete=models.CASCADE, null=True, blank=True)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  rate = models.IntegerField()
  comment = models.TextField(null=True, blank=True)

  class Meta:
    db_table = "ratings"

  def __str__(self):
    return "%s - %s - %s" % (self.customer, self.woodwork, self.rate)