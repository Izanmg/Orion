from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser  # Asegúrate de importar tu modelo
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model,authenticate

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True,error_messages={'required':"El correo electronico es obligatorio"})  # Hace obligatorio el email
    username = forms.CharField(required=True,error_messages={'required':"El nombre de usuario es obligatorio"})
    password1 = forms.CharField(required=True,error_messages={'required':"Debes ingresar una contraseña"})
    password2 = forms.CharField(required=True,error_messages={'required':"Confirma tu contraseña"})
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]


    def clean_email(self):
        email = self.cleaned_data.get("email")

        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("El correo ya esta en uso")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get("username")

        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError("El usuario ya esta en uso")
        return username 
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("Las contraseñas no coinciden")
        return password2
        

User = get_user_model()

class LoginForm(forms.Form):  
    username = forms.CharField(
        required=True,
        error_messages={'required': 'Debes especificar el usuario o correo'}
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput,
        error_messages={'required': 'Debes escribir la contraseña'}
    )
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        # Verificar si el username o email existe en la base de datos
        user = None
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)  # Obtiene el usuario por nombre de usuario
        elif User.objects.filter(email=username).exists():
            user = User.objects.get(email=username)  # Obtiene el usuario por correo electrónico
            cleaned_data['username'] = user.username

        
        if not user:
            self.add_error('username','El usuario o correo no existe')
        
        user = authenticate(username=user,password=password)

        if not user:
            self.add_error('password', 'La contraseña es incorrecta')
            return password
        
        return cleaned_data


# Hay que modificar la clase para que le pueda pasar parametros y poder acceder al usuario activo (le pasare el parametro user= request.user para pasarle el usuario activo desde views)
class UpdateForm(UserChangeForm):
    nombre = forms.CharField(required=False)
    apellidos = forms.CharField(required=False)
    username = forms.CharField(required=False)
    email = forms.EmailField(required=False)

    class Meta:
        model = get_user_model()
        fields = [
            'nombre',
            'apellidos',
            'username',
            'email',

        ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super().__init__(*args, **kwargs)


    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = str(self.user.username)
        if username == user:
            return
        elif User.objects.filter(username=username).exists():
            raise ValidationError("El usuario ya esta en uso")
        
        return username
    
class UpdatePassword(PasswordChangeForm):

    class Meta:
        model = get_user_model()
        fields = [
            'current_password',
            'new_password',
            'confirm_password'
        ]

        """current_password = cleaned_data.get('current-password')
        new_password = cleaned_data.get('new-password')
        confirm_password = cleaned_data.get('confirm-password')"""