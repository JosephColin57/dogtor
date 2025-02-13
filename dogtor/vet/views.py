from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView

# models

from .models import PetOwner

# Create your views here.

def list_pet_owners(request):
    print("REQUEST ---->", request)
    """ List Owners"""
    # Tomamos la informacion de la base de datos
    owners = PetOwner.objects.all()

    # Hacemos contexto
    context = {"owners": owners}
    print(context)

    # Conectamos el contexto
    template= loader.get_template('vet/owners/list.html')

    # Retornamos respuesta HTTP con el template pasando el contexto
    return HttpResponse(template.render(context, request))

# Vistas de class

# class OwnerList(TemplateView):
#     #Elegiumos la plantilla
#     template_name = "vet/owners/list.html"

#     # Pasamos el contexto
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["owners"] = PetOwner.objects.all()
#         return context

class OwnerList(ListView):
    # 1.- Colocamos el Modelo
    # 2.- Template que vamos a renderizar el modelo
    # 3.- Contexto que va a usar el template

    model = PetOwner # 1 
    template_name = "vet/owners/list.html" # 2
    context_object_name = "owners" # 3

class Test(View):
    # Como funcion el metodo(GET, PATCH, POST, DELETE, PUT)
    def get(self, request):
        return HttpResponse("Hello world from a class generic view")