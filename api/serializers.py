from rest_framework import serializers
from .models import Person, Place, Picture


class PersonSerializer(serializers.ModelSerializer):
    """Serializes the db model Person"""

    class Meta:
        model = Person
        fields = "__all__"
        lookup_fields = ["pk", "forename"]
        # fields = ["id", "forename", "lastname"]


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = "__all__"
