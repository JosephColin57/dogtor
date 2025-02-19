from django.urls import path, include
from rest_framework import routers

# Views
from .views import OwnersViewSet, PetsViewSet, PetDatesViewSet

# Routers
router = routers.DefaultRouter()
router.register(r"owners", OwnersViewSet)
router.register(r"pets", PetsViewSet)
router.register(r"pet-dates", PetDatesViewSet)

urlpatterns = [
    path("", include(router.urls)),
 ]
