document.addEventListener('DOMContentLoaded', () => {
    const inputs = document.querySelectorAll('.form-group input');

    inputs.forEach(input => {
        input.addEventListener('focus', () => {
            input.style.backgroundColor = '#f3f8ff';
        });

        input.addEventListener('blur', () => {
            input.style.backgroundColor = '#ffffff';
        });
    });

    const signupButton = document.querySelector('.btn-success');
    signupButton.addEventListener('click', (e) => {
        signupButton.classList.add('clicked');
        setTimeout(() => {
            signupButton.classList.remove('clicked');
        }, 300);
    });
});
