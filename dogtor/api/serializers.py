from rest_framework import serializers

# Modelos
from vet.models import PetOwner, Pet, PetDate

# Serializadores --> Representacion de nuestra API
# class OwnersSerializers(serializers.HyperlinkedModelSerializer):
#     """Pet Owners Serializer."""

#     class Meta:
#         model = PetOwner
#         fields = ["id", "first_name", "last_name", "email", "address", "phone", "created_at" ]

# class PetsSerializers(serializers.HyperlinkedModelSerializer):
#     """Pet Serializer."""

#     owner = serializers.PrimaryKeyRelatedField(queryset=PetOwner.objects.all(), many=False)

#     class Meta:
#         model = Pet
#         fields = ["id", "name", "type", "created_at", "owner" ]

# class PetDatesSerializers(serializers.ModelSerializer):
#     """Pet Dates Serializer."""
    
#     class Meta:
#         model = PetDate
#         fields = ["id", "datetime", "type", "created_at", "pet" ]

class OwnersListSerializer(serializers.ModelSerializer):
    """Serializer to list all Pet Owners."""

    class Meta:
        model = PetOwner
        fields = ["id", "first_name", "last_name"]

class OwnersDetailSerializer(serializers.ModelSerializer):
    """Serializer to show details of a Pet Owner."""

    class Meta:
        model = PetOwner
        # fields = "__all__" # Mala Practica
        fields = ["first_name", "last_name", "email", "address", "phone", "created_at"] # Buena Practica

class CreateOwnerSerializer(serializers.ModelSerializer):
    """Serializer to create a Pet Owner."""

    class Meta:
        model = PetOwner
        fields = ["first_name", "last_name", "email", "address", "phone"]

class UpdateOwnerSerializer(serializers.ModelSerializer):
    """Serializer to update a Pet Owner."""

    class Meta:
        model = PetOwner
        fields = ["first_name", "last_name", "email", "address", "phone"]

class DeleteOwnerSerializer(serializers.ModelSerializer):
    """Serializer to delete a Pet Owner."""

    class Meta:
        model = PetOwner
        fields = "__all__"