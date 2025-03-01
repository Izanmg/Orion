// Funciones para los campos de texto generales
function enableEdit(inputId, modificarId, optionsId) {
    document.getElementById(inputId).disabled = false;
    document.getElementById(modificarId).style.display = 'none';
    document.getElementById(optionsId).classList.remove('hidden');
}

function cancelEdit(inputId, modificarId, optionsId, originalValue) {
    document.getElementById(inputId).value = originalValue;
    document.getElementById(inputId).disabled = true;
    document.getElementById(optionsId).classList.add('hidden');
    document.getElementById(modificarId).style.display = 'inline-block';
}
function confirmEdit(inputId, modificarId, optionsId) {
    document.getElementById(inputId).disabled = true;
    document.getElementById(optionsId).classList.add('hidden');
    document.getElementById(modificarId).style.display = 'inline-block';
}

// Funciones específicas para el cambio de contraseña
function enablePasswordEdit() {
    document.getElementById('default-password').classList.add('hidden');
    document.getElementById('edit-options-password').classList.remove('hidden');
    document.getElementById('old_password').disabled = false;
    document.getElementById('new_password1').disabled = false;
    document.getElementById('new_password2').disabled = false;

}
function cancelPasswordEdit() {
    document.getElementById('edit-options-password').classList.add('hidden');
    document.getElementById('default-password').classList.remove('hidden');
    document.getElementById('old_password').value = '';
    document.getElementById('new_password1').value = '';
    document.getElementById('new_password2').value = '';
    document.getElementById('old_password').disabled = true;
    document.getElementById('new_password1').disabled = true;
    document.getElementById('new_password2').disabled = true;
}
function confirmPasswordEdit() {
    document.getElementById('edit-options-password').classList.add('hidden');
    document.getElementById('default-password').classList.remove('hidden');
    document.getElementById('old_password').value = '';
    document.getElementById('new_password1').value = '';
    document.getElementById('new_password2').value = '';
}

function enableProfilePicture() {
    document.getElementById("input-profile").disabled = false;
}



