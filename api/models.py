"""Lists all models"""

from django.db import models


class Person(models.Model):
    """Represents a perso and its releations"""

    id = models.BigAutoField(primary_key=True)
    forename: str = models.CharField(max_length=256)
    lastname: str = models.CharField(max_length=256)
    avatar: str = models.CharField(max_length=256, blank=True, null=True)
    birthname: str = models.CharField(max_length=256, blank=True, null=True)
    birthdate = models.DateTimeField(null=True, blank=True)
    dayOfDeath = models.DateTimeField(null=True, blank=True)
    bio: str = models.TextField(null=True, blank=True)
    marriages = models.ManyToManyField("self", symmetrical=True, blank=True)
    parents = models.ManyToManyField("self", symmetrical=False, blank=True)

    def __str__(self):
        if (self.birthname):
            return f"{self.forename} {self.lastname} ({self.birthname})"
        else:
            return f"{self.forename} {self.lastname}"



class Place(models.Model):
    """A place in the world"""

    id = models.BigAutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    desciption = models.TextField()


class Picture(models.Model):
    """A picture"""

    id = models.BigAutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    desciption = models.TextField()
