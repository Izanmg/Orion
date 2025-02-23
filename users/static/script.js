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
    document.getElementById('current-password').disabled = false;
    document.getElementById('new-password').disabled = false;
    document.getElementById('confirm-password').disabled = false;

}
function cancelPasswordEdit() {
    document.getElementById('edit-options-password').classList.add('hidden');
    document.getElementById('default-password').classList.remove('hidden');
    document.getElementById('current-password').value = '';
    document.getElementById('new-password').value = '';
    document.getElementById('confirm-password').value = '';
    document.getElementById('current-password').disabled = true;
    document.getElementById('new-password').disabled = true;
    document.getElementById('confirm-password').disabled = true;
}
function confirmPasswordEdit() {
    document.getElementById('edit-options-password').classList.add('hidden');
    document.getElementById('default-password').classList.remove('hidden');
    document.getElementById('current-password').value = '';
    document.getElementById('new-password').value = '';
    document.getElementById('confirm-password').value = '';
}