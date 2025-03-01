// Funciones para los campos de texto generales

// Activa la edición del campo de texto y muestra las opciones de modificar.
function enableEdit(inputId, modificarId, optionsId) {
    document.getElementById(inputId).disabled = false; // Habilita el campo de texto especificado por inputId.
    document.getElementById(modificarId).style.display = 'none'; // Oculta el botón "Modificar".
    document.getElementById(optionsId).classList.remove('hidden'); // Muestra las opciones de edición.
}

// Cancela la edición, restaura el valor original y deshabilita el campo de texto.
function cancelEdit(inputId, modificarId, optionsId, originalValue) {
    document.getElementById(inputId).value = originalValue; // Restaura el valor original en el campo de texto.
    document.getElementById(inputId).disabled = true; // Deshabilita el campo de texto.
    document.getElementById(optionsId).classList.add('hidden'); // Oculta las opciones de edición.
    document.getElementById(modificarId).style.display = 'inline-block'; // Muestra el botón "Modificar".
}

// Confirma la edición, deshabilita el campo de texto y oculta las opciones de edición.
function confirmEdit(inputId, modificarId, optionsId) {
    document.getElementById(inputId).disabled = true; // Deshabilita el campo de texto después de confirmar.
    document.getElementById(optionsId).classList.add('hidden'); // Oculta las opciones de edición.
    document.getElementById(modificarId).style.display = 'inline-block'; // Muestra el botón "Modificar".
}

// Funciones específicas para el cambio de contraseña

// Activa la edición de la contraseña, mostrando los campos y opciones correspondientes.
function enablePasswordEdit() {
    document.getElementById('default-password').classList.add('hidden'); // Oculta la vista predeterminada de la contraseña.
    document.getElementById('edit-options-password').classList.remove('hidden'); // Muestra las opciones de edición de la contraseña.
    document.getElementById('old_password').disabled = false; // Habilita el campo para ingresar la contraseña actual.
    document.getElementById('new_password1').disabled = false; // Habilita el campo para la nueva contraseña.
    document.getElementById('new_password2').disabled = false; // Habilita el campo para confirmar la nueva contraseña.
}

// Cancela la edición de la contraseña, restaurando la vista original y limpiando los campos.
function cancelPasswordEdit() {
    document.getElementById('edit-options-password').classList.add('hidden'); // Oculta las opciones de edición de la contraseña.
    document.getElementById('default-password').classList.remove('hidden'); // Muestra la vista predeterminada de la contraseña.
    document.getElementById('old_password').value = ''; // Limpia el campo de la contraseña actual.
    document.getElementById('new_password1').value = ''; // Limpia el campo de la nueva contraseña.
    document.getElementById('new_password2').value = ''; // Limpia el campo de confirmación de la nueva contraseña.
    document.getElementById('old_password').disabled = true; // Deshabilita el campo de la contraseña actual.
    document.getElementById('new_password1').disabled = true; // Deshabilita el campo de la nueva contraseña.
    document.getElementById('new_password2').disabled = true; // Deshabilita el campo de confirmación de la nueva contraseña.
}

// Confirma el cambio de contraseña, restaurando la vista original y limpiando los campos.
function confirmPasswordEdit() {
    document.getElementById('edit-options-password').classList.add('hidden'); // Oculta las opciones de edición de la contraseña.
    document.getElementById('default-password').classList.remove('hidden'); // Muestra la vista predeterminada de la contraseña.
    document.getElementById('old_password').value = ''; // Limpia el campo de la contraseña actual.
    document.getElementById('new_password1').value = ''; // Limpia el campo de la nueva contraseña.
    document.getElementById('new_password2').value = ''; // Limpia el campo de confirmación de la nueva contraseña.
}

// Habilita el campo para cambiar la imagen de perfil.
function enableProfilePicture() {
    document.getElementById("input-profile").disabled = false; // Activa el campo de selección de la imagen de perfil.
}
