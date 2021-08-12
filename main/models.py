from django.db import models

class Movie(models.Model):
  title = models.CharField(max_length=45)
  description = models.TextField()
  release_date = models.DateTimeField()
  duration = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __repr__(self):
    return f"Title {self.title}, Description: {self.description}, release date: {self.release_date},  duration: {self.duration}"

class Wizard(models.Model):
  name = models.CharField(max_length=45)
  house = models.CharField(max_length=45)
  pet = models.CharField(max_length=45)
  year = models.IntegerField()

class Users(models.Model):
  first_name = models.CharField(max_length=45)
  last_name = models.CharField(max_length=45)
  email_adress = models.CharField(max_length=45)
  age = models.IntegerField()

  def __repr__(self):
    return f"Username: {self.first_name} {self.last_name}, {self.age} years old. Email: {self.email_adress}"

class Dojos(models.Model):
  name = models.CharField(max_length=45)
  city = models.CharField(max_length=45)
  state = models.CharField(max_length=2)
  desc = models.CharField(max_length=45, default='Old Dojo')
  def __repr__(self):
    return f"{self.name} Dojo, {self.desc}"

class Ninjas(models.Model):
  first_name = models.CharField(max_length=45)
  last_name = models.CharField(max_length=45)
  state = models.CharField(max_length=45)
  dojos = models.ForeignKey(Dojos, related_name='dojo', on_delete = models.CASCADE)
  def __repr__(self):
    return f"Ninja: {self.first_name} {self.last_name} from {self.state} part of {self.dojos} Dojo"
