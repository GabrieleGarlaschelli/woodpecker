from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser

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
