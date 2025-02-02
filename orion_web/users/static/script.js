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
});
