document.addEventListener('DOMContentLoaded', function() {
    const inputElements = document.querySelectorAll('input[name="quantity"]');
    inputElements.forEach(function(input) {
        input.addEventListener('input', function(event) {
            event.target.value = event.target.value.replace(/\D/g, '');
        });
    });
});