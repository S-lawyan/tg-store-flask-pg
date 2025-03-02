
function cartManage(event, productId) {
    event.preventDefault();
    // const user = Telegram.WebApp.initDataUnsafe.user;
    // const userId = user.id;
    const userId = '';

    if (!event.target.querySelector('input[name="user_id"]')) {
        const userIdInput = document.createElement('input');
        userIdInput.type = 'hidden';
        userIdInput.name = 'user_id';
        userIdInput.value = userId;
        event.target.appendChild(userIdInput);
    }

    const cartButton = event.target.querySelector('button[type="submit"]');
    const formData = new FormData(event.target);
    const cart_button_state = cartButton.getAttribute('data-state');

    if (cart_button_state === 'add') {
        const url = '/add_to_cart';
        addToCart(event, url, productId, formData);
    }

    if (cart_button_state === 'rm') {
        const url = '/remove_from_cart';
        removeFromBasket(event, url, productId, formData);
    }

}

function addToCart(event, url, productId, formData) {

        // Отправляем POST-запрос на сервер
        fetch(
            url,
            {method: 'POST', body: formData,}
        ).then(response => response.json()).then(data => {
            if (data.success) {
                // Обновляем кнопки
                const button_basket = event.target.querySelector('button[type="submit"]');
                button_basket.innerHTML = '✓ В корзине';
                button_basket.setAttribute('data-state', 'rm');
                const quantityButtons = event.target.querySelectorAll('button.button_quantity');
                quantityButtons.forEach(button => button.disabled = true);
                event.target.querySelector('input[name="quantity"]').readOnly = true;
            } else {
                alert('Ошибка: ' + (data.error || 'Неизвестная ошибка'));
            }
        })
        .catch(error => {
            console.error('Ошибка:', error);
            alert('Произошла ошибка при отправке запроса на добавление в корзину');
        });
}

function removeFromBasket(event, url, productId, formData) {

        // Отправляем POST-запрос на сервер
        fetch(
            url,
            {method: 'POST', body: formData,}
        ).then(response => response.json()).then(data => {
            if (data.success) {
                // Обновляем кнопки
                const button_basket = event.target.querySelector('button[type="submit"]');
                button_basket.innerHTML = 'В корзину';
                button_basket.setAttribute('data-state', 'add');
                const quantityButtons = event.target.querySelectorAll('button.button_quantity');
                quantityButtons.forEach(button => button.disabled = false);
                // Устанавливаем количество товара в 1
                event.target.querySelector('input[name="quantity"]').value = 1;
                event.target.querySelector('input[name="quantity"]').readOnly = false;
            } else {
                alert('Ошибка: ' + (data.error || 'Неизвестная ошибка'));
            }
        })
        .catch(error => {
            console.error('Ошибка:', error);
            alert('Произошла ошибка при отправке запроса на удаление из корзины');
        });
}

function changeQuantity(productId, delta) {
    const input = document.getElementById(`quantity_${productId}`);
    let quantity = parseInt(input.value) + delta;
    if (quantity < 1) quantity = 1; // Минимум 1 товар
    input.value = quantity;
}
