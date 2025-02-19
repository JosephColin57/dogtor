from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import  OwnersListSerializer, OwnersDetailSerializer

#Models
from vet.models import PetOwner, Pet, PetDate

# Create your views here.
# class OwnersViewSet(viewsets.ModelViewSet):
#     """ViewSet del modelo PetOwner"""

#     # 1.- queryset que se va a realizar --> Se realiza con el ORM
#     # 2.- el serializador

#     # Obtener todos los owners --> ORM seria PetOwner.objects.all()
#     queryset = PetOwner.objects.all()
#     # Serializar 
#     serializer_class = OwnersSerializers

# class PetsViewSet(viewsets.ModelViewSet):
#     """ViewSet del modelo Pet"""

#     queryset = Pet.objects.all()
#     serializer_class = PetsSerializers

# class PetDatesViewSet(viewsets.ModelViewSet):
#     """ViewSet del modelo PetDate"""

#     queryset = PetDate.objects.all()
#     serializer_class = PetDatesSerializers

class ListOwnersAPIView(generics.ListAPIView):
    """List Owners Api View."""

    queryset = PetOwner.objects.all().order_by("created_at")
    serializer_class = OwnersListSerializer

class RetrieveOwnerAPIView(generics.RetrieveAPIView):
    """Retrieve Owner Api View."""

    queryset = PetOwner.objects.all()
    serializer_class = OwnersDetailSerializer
