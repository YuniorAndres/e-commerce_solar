from django.contrib.auth.models import AbstractUser

# Extiende el modelo de usuario por si necesitas más adelante más campos personalizados
class CustomUser(AbstractUser):
    pass
