// Menu mobile
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    
    if (hamburger) {
        hamburger.addEventListener('click', function() {
            navMenu.style.display = navMenu.style.display === 'flex' ? 'none' : 'flex';
        });
    }
    
    // Auto-hide messages after 5 seconds
    const messages = document.querySelector('.messages');
    if (messages) {
        setTimeout(() => {
            messages.style.display = 'none';
        }, 5000);
    }
});