from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser  # Asegúrate de importar tu modelo
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True, error_messages={'required': "El correo electrónico es obligatorio."})  # Hace obligatorio el email
    username = forms.CharField(required=True, error_messages={'required': "El nombre de usuario es obligatorio."})
    password1 = forms.CharField(required=True, error_messages={'required': "Debes ingresar una contraseña."})
    password2 = forms.CharField(required=True, error_messages={'required': "Confirma tu contraseña."})
    
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("El correo electrónico ya está en uso.")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get("username")

        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError("El nombre de usuario ya está en uso.")
        return username 
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("Las contraseñas no coinciden.")
        return password2

class LoginForm(forms.Form):  
    username = forms.CharField(
        required=True,
        error_messages={'required': 'Debes especificar el usuario o el correo electrónico.'}
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput,
        error_messages={'required': 'Debes escribir la contraseña.'}
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
            raise ValidationError({'username':'El usuario o el correo electrónico no existe.'})
        
        user = authenticate(username=user, password=password)

        if not user:
            raise ValidationError({'password':'La contraseña es incorrecta.'})
        
        return cleaned_data


class UpdateForm(UserChangeForm):
    nombre = forms.CharField(required=False)
    apellidos = forms.CharField(required=False)
    username = forms.CharField(required=False)
    email = forms.EmailField(required=False)

    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = str(self.user.username)
        if username == user:
            return
        elif User.objects.filter(username=username).exists():
            raise ValidationError("El nombre de usuario ya está en uso.")
        
        return username
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        user_first_name = str(self.user.first_name)
        if first_name == user_first_name:
            return
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        user_last_name = str(self.user.last_name)
        if last_name == user_last_name:
            return
        return last_name
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_email = str(self.user.email)
        if email != '':
            if email == user_email:
                return
            elif User.objects.filter(email=email).exists():
                raise ValidationError("El correo electrónico ya está en uso.")
        return email

class UpdatePassword(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput, required=True, error_messages={'required': 'Este campo es requerido.'})
    new_password1 = forms.CharField(widget=forms.PasswordInput, required=True, error_messages={'required': 'Este campo es requerido.'})
    new_password2 = forms.CharField(widget=forms.PasswordInput, required=True, error_messages={'required': 'Este campo es requerido.'})

    class Meta:
        model = get_user_model()
        fields = [
            'old_password',
            'new_password1',
            'new_password2'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Personalizar errores de new_password1
        self.fields["new_password1"].error_messages.update({
            "password_too_similar": "La nueva contraseña es demasiado similar a tu información personal.",
            "password_too_short": "La nueva contraseña debe tener al menos 8 caracteres.",
            "password_too_common": "La nueva contraseña es demasiado común.",
            "password_entirely_numeric": "La nueva contraseña no puede contener solo números.",
        })

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise ValidationError('La contraseña actual es incorrecta.')
        return old_password
    
    def clean_new_password1(self):
        new_password1 = self.cleaned_data.get("new_password1")
        if not new_password1:
            raise ValidationError("Este campo no puede estar vacío.")
        return new_password1
    
    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        

        if new_password1 != new_password2:
            raise ValidationError({"new_password2": "Las contraseñas no coinciden."})
        if self.user.check_password(new_password2):
            raise ValidationError({"new_password1": "La nueva contraseña no puede ser igual a la actual.",
                                   "new_password2": "La nueva contraseña no puede ser igual a la actual."})
        return cleaned_data


class ImgForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=True, error_messages={"required": "Este campo es requerido."})

    class Meta:
        model = get_user_model()
        fields = ['profile_picture']
