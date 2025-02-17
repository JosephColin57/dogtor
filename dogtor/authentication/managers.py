from django.contrib.auth.models import BaseUserManager

class ModUserManager(BaseUserManager):
    """ Mod User Custom Manager"""

    # 1.- create_user
    # creamos el de joel -> Patos5783

    def create_user(self, email, user_name, first_name, password, **others_fields):
        """Overriding create_user func for ModUserManager """

        #se pueden agregar validaciones
        if not email:
            raise ValueError("You must provide an email.")

        # Se coloca en minuscula el correo
        email = self.normalize_email(email)

        # Nos hizo el usuario en la variable "user"
        user = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)

        # Seteamos Password
        user.set_password(password)

        # Guardar en Base de datos
        user.save()

        return user

    # 2.- create_superuser
    # creamos el de admin -> Patos5783

    def create_superuser(self, email, user_name, first_name, password, **others_fields):
        """Overriding create_superuser func for ModUserManager """

        # Vamos a colocar el is_staff --> True, is_active --> True, is_superuser --> True
        others_fields.setdefault("is_staff", True)
        others_fields.setdefault("is_active", True)
        others_fields.setdefault("is_superuser", True)
        
        # Creamos el usuario con la funcion recien creada de create_user 
        return self.create_user(email, user_name, first_name, password, **others_fields)