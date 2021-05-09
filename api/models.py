from django.db import models

# Create your models here.


class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    forename: str = models.CharField(max_length=256)
    lastname: str = models.CharField(max_length=256)
    avatar: str = models.CharField(max_length=256, blank=True, null=True)
    birthname: str = models.CharField(max_length=256, blank=True, null=True)
    birthdate = models.DateTimeField(null=True, blank=True)
    dayOfDeath = models.DateTimeField(null=True, blank=True)
    bio: str = models.TextField()
    marriages = models.ManyToManyField("self", symmetrical=True)
    parents = models.ManyToManyField("self", symmetrical=True)
    children = models.ManyToManyField("self", symmetrical=True)


class Places(models.Model):
    id = models.BigAutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    desciption = models.TextField()


class Foto(models.Model):
    id = models.BigAutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    desciption = models.TextField()
