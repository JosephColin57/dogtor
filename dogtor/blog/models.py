from django.db import models

# Create your models here.

class Post(models.Model):
    """Model Post"""

    name= models.CharField(max_length=50),
    description = models.TextField(max_length=1000, blank=True, null=True)

# blank=True, null=True -> para que no sea obligatorio

# blank=True -> en el formulario/Django puede estar vacio
# null=True -> en la base de datos puede estar vacio

    def __str__(self):
        return f"{self.pk}: {self.name}"