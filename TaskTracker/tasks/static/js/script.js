document.addEventListener('DOMContentLoaded', function () {
    const successMessage = document.querySelector('.success-message');
    if (successMessage) {
        // Başarı mesajı 3 saniye sonra kaybolur
        setTimeout(() => {
            successMessage.style.display = 'none';
        }, 3000);
    }
});