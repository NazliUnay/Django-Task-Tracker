document.addEventListener('DOMContentLoaded', function () {
    const successMessage = document.querySelector('.success-message');
    if (successMessage) {
        // Başarı mesajı 3 saniye sonra kaybolur
        setTimeout(() => {
            successMessage.style.display = 'none';
        }, 3000);
    }

    const hamburger = document.getElementById('hamburger');
    const menu = document.getElementById('menu');
    const overlay = document.getElementById('overlay');

    if (hamburger && menu && overlay) {
        hamburger.addEventListener('click', () => {
            menu.classList.toggle('active');
            overlay.classList.toggle('active');
        });

        overlay.addEventListener('click', () => {
            menu.classList.remove('active');
            overlay.classList.remove('active');
        });
    }
});
