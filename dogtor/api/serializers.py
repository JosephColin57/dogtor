from rest_framework import serializers

# Modelos
from vet.models import PetOwner, Pet, PetDate

# Serializadores --> Representacion de nuestra API
class OwnersSerializers(serializers.HyperlinkedModelSerializer):
    """Pet Owners Serializer."""

    class Meta:
        model = PetOwner
        fields = ["id", "first_name", "last_name", "email", "address", "phone", "created_at" ]

class PetsSerializers(serializers.ModelSerializer):
    """Pet Serializer."""

    class Meta:
        model = Pet
        fields = ["id", "name", "type", "created_at", "owner" ]

class PetDatesSerializers(serializers.ModelSerializer):
    """Pet Dates Serializer."""
    
    class Meta:
        model = PetDate
        fields = ["id", "datetime", "type", "created_at", "pet" ]