document.addEventListener("DOMContentLoaded", function () {
    // Añadir la funcionalidad de mostrar/ocultar campos del formulario de registro
    const nextStepButton = document.getElementById("next-step");
    const stepBackButton = document.getElementById("step-back");
    const firstStep = document.getElementById("first-step");
    const secondStep = document.getElementById("second-step");

    nextStepButton.addEventListener("click", function () {
        // Ocultar el primer paso (Nombre, Apellidos, Nombre de usuario)
        firstStep.classList.add("hidden");
        
        // Mostrar el segundo paso (Correo electrónico, Contraseña, Confirmar Contraseña)
        secondStep.classList.remove("hidden");

        stepBackButton.classList.remove("hidden");
    });

    stepBackButton.addEventListener("click", function () {
        // Mostrar el primer paso
        firstStep.classList.remove("hidden");
        
        // Ocultar el segundo paso
        secondStep.classList.add("hidden");
    
        // Ocultar el botón de "Atrás" porque estamos en el primer paso
        stepBackButton.classList.add("hidden");
    });
    
    
});
