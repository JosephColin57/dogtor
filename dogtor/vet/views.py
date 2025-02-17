from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from .forms import OwnerForm, PetForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

# models

from .models import PetOwner, Pet

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
    template = loader.get_template("vet/owners/list.html")

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


class Petlist(ListView):
    """Render all Pets."""

    model = Pet
    template_name = "vet/pets/list.html"
    context_object_name = "pets"


class PetDetail(DetailView):
    """Render a details of a specific pet with pk"""

    model = Pet
    template_name = "vet/pets/detail.html"
    context_object_name = "pet"


class OwnerList(ListView):
    """Render all Pet Owners."""

    # 1.- Colocamos el Modelo
    # 2.- Template que vamos a renderizar el modelo
    # 3.- Contexto que va a usar el template

    model = PetOwner  # 1
    template_name = "vet/owners/list.html"  # 2
    context_object_name = "owners"  # 3


class OwnerDetail(LoginRequiredMixin, DetailView):
    """Renders a specific Owner with their pk."""

    model = PetOwner
    template_name = "vet/owners/detail.html"
    context_object_name = "owner"


class Test(View):
    # Como funcion el metodo(GET, PATCH, POST, DELETE, PUT)
    def get(self, request):
        return HttpResponse("Hello world from a class generic view")


class OwnersCreate(CreateView):
    """Create a new Owner."""

    # 1.- Model
    # 2.- Template a Renderizar
    # 3.- Campos que va a tener el formulario
    # 4.- URLs si la request fue exitosa --> reversed_url

    model = PetOwner  # 1
    template_name = "vet/owners/create.html"  # 2
    form_class = OwnerForm  # 3
    success_url = reverse_lazy("vet:owners_list")  # 4


class OwnersUpdate(PermissionRequiredMixin, UpdateView):
    """Update informacion of owner"""

    # Permiso que se necesita ṕara ingresar
    permission_required = "vet.change_petowner"
    raise_exception = False
    login_url = "/admin/login/" # En caso de que la sesion no este iniciada
    redirect_field_name = "next"

    model = PetOwner
    template_name = "vet/owners/update.html"
    form_class = OwnerForm
    success_url = reverse_lazy("vet:owners_list")


class PetCreate(CreateView):
    """Create a new Pet."""

    model = Pet
    template_name = "vet/pets/create.html"
    form_class = PetForm
    success_url = reverse_lazy("vet:pets_list")


class PetsUpdate(UpdateView):
    """Update informacion of Pet"""

    model = Pet
    template_name = "vet/pets/update.html"
    form_class = PetForm
    success_url = reverse_lazy("vet:pets_list")
