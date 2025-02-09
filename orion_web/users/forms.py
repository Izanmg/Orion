from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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

        # Verificar si el username existe en la base de datos
        user = None
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)  # Obtiene el usuario por nombre de usuario
        elif User.objects.filter(email=username).exists():
            user = User.objects.get(email=username)  # Obtiene el usuario por correo electrónico
            cleaned_data['username'] = user


        
        if not user:
            self.add_error('username','El usuario o correo no existe')
            raise forms.ValidationError("El usuario o correo no existe.")
        
        user = authenticate(username=user,password=password)

        if not user:
            self.add_error('password', 'La contraseña es incorrecta')
            print("Aqui ha entrado")
            print(user)

            return password
        return cleaned_data
