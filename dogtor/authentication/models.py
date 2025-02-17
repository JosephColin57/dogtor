from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

# Create your models here.

# maneger

class ModUser(AbstractUser, PermissionsMixin):
    """Custom modereator User."""
# sobreescribir propiedades del modelo usuario y atributos de la tabla de user
# extender propiedades o atributos (nuevos fields)

    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=200, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    about = models.TextField(max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    # Campo identificador de la tabla
    USERNAME_FIELD = "email"

    # Campos requeridos para crear al createsuperuser
    REQUIRED_FIELDS = ["user_name"]

    # Metodo String
    def __str__(self):
        return f"{self.user_name} {self.email}"
