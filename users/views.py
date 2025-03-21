from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import UserForm, LoginForm, UpdateForm, UpdatePassword, ImgForm
import os
# Este archivo contiene las vistas que gestionan el registro, inicio de sesión, actualización de perfil y cierre de sesión.

def index(request):
    # Vista que muestra la página de inicio.
    return render(request, 'index.html')


@login_required
def home(request):
    # Vista que muestra la página de inicio de sesión del usuario (requiere estar autenticado).
    if request.method == "POST":
        # Inicialización de formularios para distintos tipos de actualización (contraseña, imagen, datos).
        form_password = None
        form_image = None
        form_data = None

        # Si el usuario sube una nueva imagen de perfil.
        if "profile_picture" in request.FILES:
            form_image = ImgForm(request.POST, request.FILES, instance=request.user)
        
        # Si el usuario quiere actualizar su contraseña.
        elif "old_password" in request.POST and "new_password1" in request.POST and "new_password2" in request.POST:
            form_password = UpdatePassword(user=request.user, data=request.POST)
        
        # Si el usuario quiere actualizar sus datos de perfil.
        else:
            form_data = UpdateForm(request.POST, user=request.user)
        
        # Si se recibe un formulario de actualización de datos (nombre, email, etc.)
        if form_data:
            if form_data.is_valid():
                # Si los campos son válidos, actualizamos los datos del usuario.
                if form_data.cleaned_data.get('username'):
                    user = request.user
                    user.username = form_data.cleaned_data.get('username')
                    user.save()
                elif form_data.cleaned_data.get('first_name'):
                    user = request.user
                    user.first_name = form_data.cleaned_data.get('first_name')
                    user.save()
                elif form_data.cleaned_data.get('last_name'):
                    user = request.user
                    user.last_name = form_data.cleaned_data.get('last_name')
                    user.save()
                elif form_data.cleaned_data.get('email'):
                    user = request.user
                    user.email = form_data.cleaned_data.get('email')
                    user.save()
            else:
                # Si el formulario es inválido, se vuelve a renderizar la vista con los errores del formulario.
                return render(request, "home.html", {"form": form_data})
            # Si los cambios son correctos, se redirige al usuario a la misma página de inicio.
            return redirect("home")
        
        # Si se recibe un formulario para cambiar la contraseña.
        elif form_password:
            if form_password.is_valid():
                user = request.user
                # Se actualiza la contraseña y se asegura de que la sesión no expire.
                user.set_password(form_password.cleaned_data.get("new_password2"))
                user.save()
                update_session_auth_hash(request, user)
            else:
                return render(request, "home.html", {"form": form_password})

        # Si se recibe un formulario para actualizar la imagen de perfil.
        elif form_image:
            if form_image.is_valid():
                User = get_user_model()
                user = request.user
                user_obj = User.objects.get(id=user.id)
                profile_picture_content = user_obj.profile_picture
                old_img_path = user_obj.profile_picture.path
                form_image.save()  # Se guarda la nueva imagen.

                # Si la imagen es diferente de la predeterminada y existe una imagen antigua, se elimina.
                if profile_picture_content != "/profiles/default_profile_picture.jpg" and os.path.exists(old_img_path):
                    os.remove(old_img_path)
            else:
                return render(request, "home.html", {"form": form_image})

        # Redirige al usuario a la página de inicio de sesión después de completar la acción.
        return redirect("home")
    
    # Si no es una solicitud POST, se renderiza la página de inicio de sesión del usuario.
    return render(request, "home.html")


def login_view(request):
    # Vista para manejar el inicio de sesión de los usuarios.
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            # Se intenta autenticar al usuario con las credenciales proporcionadas.
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Si la autenticación es exitosa, el usuario inicia sesión.
                return redirect("home")
        else:
            return render(request, "login.html", {"form": form})
    
    # Si no es una solicitud POST, se muestra el formulario de inicio de sesión vacío.
    form = LoginForm()
    return render(request, "login.html", {"form": form})


def register(request):
    # Vista para manejar el registro de nuevos usuarios.
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # Se guarda el nuevo usuario.
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            # El usuario se autentica automáticamente después de registrarse.
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("home")
        else:
            # Si el formulario es inválido, se renderiza la vista con los errores.
            return render(request, "register.html", {"form": form})

    # Si no es una solicitud POST, se muestra el formulario de registro vacío.
    form = UserForm()
    return render(request, "register.html", {"form": form})


def logout_view(request):
    # Vista para cerrar sesión del usuario.
    logout(request)
    return redirect("index")

def delete_acount(request):
    if request.user.is_authenticated:
        request.user.delete()
        return redirect("index")
    
    return redirect("log")