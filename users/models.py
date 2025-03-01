from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    # Campo para almacenar la imagen de perfil del usuario.
    profile_picture = models.ImageField(
        upload_to="profiles/",  # Carpeta dentro del directorio media donde se guardarán las imágenes.
        blank=True,  # Permite que este campo quede vacío.
        null=True,  # Permite que este campo sea nulo en la base de datos.
        default="/profiles/default_profile_picture.jpg"  # Imagen predeterminada si el usuario no tiene una imagen de perfil.
    )
