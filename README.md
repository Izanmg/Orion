# Orion - Interfaz Web de Registro y Login

Este proyecto es una interfaz web desarrollada con Django y estilizada con Tailwind CSS. Permite a los usuarios registrarse, iniciar sesión, actualizar su perfil (incluyendo nombre, apellidos, nombre de usuario, correo electrónico y foto de perfil), cambiar su contraseña y cerrar sesión. La aplicación utiliza una base de datos SQLite para almacenar la información de los usuarios y sus imágenes de perfil.

## Tecnologías Utilizadas
- **Python** (3.8 o superior)
- **Django** (5.1.5)
- **HTML**
- **Tailwind CSS** (vía CDN)
- **JavaScript** (para interacciones en la interfaz)
- **SQLite** (base de datos predeterminada)

## Instalación

Sigue estos pasos para configurar el proyecto localmente:

### 1. Clonar el repositorio
```bash
    git clone https://github.com/Izanmg/Orion.git
    cd [tu-repositorio]
```

### 2. Crear y activar un entorno virtual
```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
Asegúrate de tener un archivo `requirements.txt` con las dependencias necesarias. Si no lo tienes, puedes crearlo con:
```bash
    pip freeze > requirements.txt
```
Luego, instala las dependencias:
```bash
    pip install -r requirements.txt
```

### 4. Configurar Tailwind CSS
Este proyecto utiliza Tailwind CSS a través del CDN, por lo que no es necesario instalar ninguna dependencia adicional para el front-end. El enlace al CDN ya está incluido en las plantillas HTML.

### 5. Aplicar migraciones para la base de datos
```bash
    python manage.py migrate
```

### 6. Iniciar el servidor
```bash
    python manage.py runserver
```

Abre tu navegador en [http://localhost:8000](http://localhost:8000) para ver la aplicación.

## Uso

- **Página Principal:** Accede a [http://localhost:8000/](http://localhost:8000/) para ver la página de inicio, donde puedes elegir entre iniciar sesión o registrarte.
- **Registro:** Visita [http://localhost:8000/register/](http://localhost:8000/register/) para crear una nueva cuenta.
- **Login:** Usa [http://localhost:8000/login/](http://localhost:8000/login/) para iniciar sesión con tus credenciales.
- **Perfil de Usuario:** Una vez logueado, accede a [http://localhost:8000/home/](http://localhost:8000/home/) para ver y actualizar tu información de perfil, incluyendo la foto de perfil, nombre, apellidos, nombre de usuario, correo electrónico y contraseña.
- **Cerrar Sesión:** Haz clic en "Cerrar Sesión" para salir de tu cuenta y volver a la página principal.

## Estructura del Proyecto
```
.
├── manage.py  # Archivo principal para ejecutar comandos de Django
├── orion_backend/  # Configuración principal de Django
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
├── users/  # Aplicación que maneja la lógica de usuarios
│   ├── forms.py  # Formularios para registro, login, actualización de perfil y cambio de contraseña
│   ├── models.py  # Modelo personalizado de usuario con campo para foto de perfil
│   ├── views.py  # Vistas para manejar las solicitudes de las páginas
│   ├── urls.py  # Rutas URL para las vistas de la aplicación
│   ├── validators.py  # Validadores personalizados para contraseñas
├── media/  # Carpeta para almacenar archivos multimedia, como las fotos de perfil de los usuarios
├── static/  # Archivos estáticos, como CSS, JavaScript e imágenes utilizadas en la interfaz
├── templates/  # Plantillas HTML
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── home.html
```

## Contribuciones
Este proyecto no está abierto a contribuciones externas en este momento. Si tienes sugerencias o encuentras algún error, por favor crea un issue en el repositorio.


