let login_form = document.querySelector('.login-form');
let register_form = document.querySelector('.register-form');


function openRegisterForm() {
    register_form.style.display = 'block';
    login_form.style.display = 'none';
}
function openLoginForm() {
    register_form.style.display = 'none';
    login_form.style.display = 'block';
}