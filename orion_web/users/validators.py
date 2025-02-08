from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth.password_validation import (
    UserAttributeSimilarityValidator,
    MinimumLengthValidator,
    CommonPasswordValidator,
    NumericPasswordValidator,
)

# 1. Validador para evitar que la contraseña sea muy similar a los atributos del usuario
class CustomUserAttributeSimilarityValidator(UserAttributeSimilarityValidator):
    def get_help_text(self):
        return _("La contraseña es demasiado similar a tus datos personales")

    def validate(self, password, user=None):
        try:
            super().validate(password, user)
        except ValidationError:
            raise ValidationError(_("La contraseña es demasiado similar a tu nombre de usuario o correo"), code='password_too_similar')

# 2. Validador para la longitud mínima
class CustomMinimumLengthValidator(MinimumLengthValidator):
    def get_help_text(self):
        return _("Contraseña demasiado corta") % {'min_length': self.min_length}

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _("Contraseña demasiado corta") % {'min_length': self.min_length},
                code='password_too_short',
            )

# 3. Validador para contraseñas comunes
class CustomCommonPasswordValidator(CommonPasswordValidator):
    def get_help_text(self):
        return _("Elige una contraseña menos común")

    def validate(self, password, user=None):
        # La lista de contraseñas comunes la usa el validador original
        if password.lower() in self.passwords:
            raise ValidationError(
                _("Esta contraseña es demasiado común"),
                code='password_too_common',
            )

# 4. Validador para contraseñas numéricas
class CustomNumericPasswordValidator(NumericPasswordValidator):
    def get_help_text(self):
        return _("La contraseña no puede ser únicamente numérica")

    def validate(self, password, user=None):
        if password.isdigit():
            raise ValidationError(
                _("La contraseña no puede ser solamente numérica"),
                code='password_entirely_numeric',
            )
