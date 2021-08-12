from django.db import models
from django.db.models.fields.related import ManyToManyField

class Books(models.Model):
  title = models.CharField(max_length=45)
  desc = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __repr__(self):
    return f"Title {self.title}, Description: {self.desc}"

class Authors(models.Model):
  first_name = models.CharField(max_length=45)
  last_name = models.CharField(max_length=45)
  notes = models.CharField(max_length=45, null=True)
  books = ManyToManyField(Books, related_name='authors')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __repr__(self):
    return f"{self.first_name} {self.last_name}"