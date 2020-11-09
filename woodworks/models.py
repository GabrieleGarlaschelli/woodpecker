from django.db import models

class Woodwork(models.Model):
  title = models.TextField()
  description = models.TextField()
  publication_date = models.DateTimeField()
  created_at = models.DateTimeField()

  class Meta:
    db_table = "woodworks"

  def __str__(self):
    return self.title + " - " + self.description
