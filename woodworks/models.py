from django.db import models

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
  
  short_description = property(_short_description)
