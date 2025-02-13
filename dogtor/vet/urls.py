from django.urls import path

# Importamos la vista
from .views import list_pet_owners, Test, OwnerList

# Vistas Funcionales -> son las vistas por defecto -> snake_case
# Vistas de Clase -> son las vistas que se crean a partir de la clase View y se le debe de poner -> as_view() -> PascalCase modelos o vistas de clase

urlpatterns = [
    path("owners", OwnerList.as_view()),
    path("test/", Test.as_view()),
]