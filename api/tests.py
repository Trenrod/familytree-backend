from django.test import TestCase
from .models import Person

# Create your tests here.


class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(forename="Albert")
        Person.objects.create(forename="Anastazija")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        albert = Person.objects.get(forename="Albert")
        anastazija = Person.objects.get(forename="Anastazija")
