from django.shortcuts import render
from rest_framework import viewsets

#Models
from vet.models import PetOwner

# Create your views here.
class OwnersViewSet(viewsets.ModelViewSet):
    """ViewSet del modelo PetOwner"""

    # 1.- queryset que se va a realizar --> Se realiza con el ORM
    # 2.- el serializador

    # Obtener todos los owners --> ORM seria PetOwner.objects.all()
    queryset = PetOwner.objects.all()
    # Serializar 

