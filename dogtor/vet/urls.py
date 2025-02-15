from django.urls import path

# Importamos la vista
from .views import list_pet_owners, Test, OwnerList, OwnerDetail, Petlist, PetDetail, OwnersCreate,OwnersUpdate, PetCreate, PetsUpdate

# Vistas Funcionales -> son las vistas por defecto -> snake_case
# Vistas de Clase -> son las vistas que se crean a partir de la clase View y se le debe de poner -> as_view() -> PascalCase modelos o vistas de clase


# alias (reversed urls) -> rutas de una app en especifico
# alias (reversed urls) -> rutas del proyecto

# si no tienes include -> reversed url se pone como 3er parametro ejemplo -> name="owners_list"
# si SI tienes include -> reversed url se pone como 2do parametro DENTRO del include() -> include(("vet.urls", "vet"))

# SINTAXIS de como acceder
# "vet:owners_list"
# "vet:owners_detail"
# "reversed_url_app:reversed_url_singular"

urlpatterns = [
    path("owners", OwnerList.as_view(), name="owners_list"),  # Sin include
    path("owners/<int:pk>", OwnerDetail.as_view(), name="owners_detail"),
    path("pets", Petlist.as_view(), name="pets_list"),
    path("pets/<int:pk>", PetDetail.as_view(), name="pets_detail"),
    path("test/", Test.as_view()),
    path("owners/add/", OwnersCreate.as_view(), name="owners_create"),
    path("owners/<int:pk>/edit/", OwnersUpdate.as_view(), name="owners_edit"),
    path("pets/add/", PetCreate.as_view(), name="pets_create"),
    path("pets/<int:pk>/edit/", PetsUpdate.as_view(), name="pets_edit"),
]
