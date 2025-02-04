document.addEventListener("DOMContentLoaded", function () {
    const btnLogin = document.getElementById("btn-login");
    const btnRegister = document.getElementById("btn-register");
    const loginForm = document.getElementById("login-form");
    const registerForm = document.getElementById("register-form");

    // Mostrar el formulario de registro si está en la URL
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get("form") === "register") {
        loginForm.classList.add("hidden");
        registerForm.classList.remove("hidden");
        btnLogin.classList.remove("hidden");
        btnRegister.classList.add("hidden");
    }

    // Cambiar entre formularios al hacer clic en los botones
    btnLogin.addEventListener("click", function () {
        loginForm.classList.remove("hidden");
        registerForm.classList.add("hidden");
        btnLogin.classList.add("hidden");
        btnRegister.classList.remove("hidden");
    });

    btnRegister.addEventListener("click", function () {
        loginForm.classList.add("hidden");
        registerForm.classList.remove("hidden");
        btnLogin.classList.remove("hidden");
        btnRegister.classList.add("hidden");
    });

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
