const cards = document.querySelectorAll('.card');

// Add blur effect only to the hovered card
cards.forEach(card => {
    card.addEventListener('mouseenter', () => {
        card.style.filter = 'blur(5px)'; // Apply blur to the card being hovered
    });
    card.addEventListener('mouseleave', () => {
        card.style.filter = 'none'; // Remove blur when not hovering
    });
});
