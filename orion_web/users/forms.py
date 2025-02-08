from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Asegúrate de importar tu modelo
from django.core.exceptions import ValidationError

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
        


