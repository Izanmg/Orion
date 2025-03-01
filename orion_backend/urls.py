"""
URL configuration for orion_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # Importa la vista de administración de Django.
from django.urls import path, include  # Importa las funciones para definir rutas y incluir otras configuraciones de URL.
from django.conf import settings  # Importa la configuración del proyecto.
from django.conf.urls.static import static  # Importa la función para servir archivos estáticos y de medios en modo desarrollo.

# Aquí se definen las rutas principales del proyecto.
urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para acceder a la vista de administración de Django (ej. http://localhost:8000/admin/).
    path('', include('users.urls')),  # Incluye las URLs de la aplicación 'users', las cuales están definidas en 'users.urls'.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Sirve archivos de medios (como imágenes) durante el desarrollo.
