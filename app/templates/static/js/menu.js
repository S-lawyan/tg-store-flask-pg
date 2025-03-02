function menuOnClick() {
    document.getElementsByClassName("burger-bar")[0].classList.toggle("burger-bar-active");
    document.getElementsByClassName("appearing_menu")[0].classList.toggle("appearing_menu_active");

};
function menuOffClick() {
    document.getElementsByClassName("burger-bar")[0].classList.remove("burger-bar-active");
    document.getElementsByClassName("appearing_menu")[0].classList.remove("appearing_menu_active");

};


// function handleCategoryClick(event) {
//     event.preventDefault(); // Отменяем стандартное поведение ссылки
//
//     // Получаем id категории из атрибута data-category
//     const categoryId = event.target.getAttribute('data-category');
//
//     // Отправляем запрос на сервер Flask
//     fetch('/category', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({ category: categoryName }), // Отправляем имя категории
//     })
//     .then(response => response.json())
//     .then(data => {
//         // Обрабатываем ответ от сервера (если нужно)
//         console.log(data);
//         // Перенаправляем пользователя на другую страницу (если нужно)
//         window.location.href = `/category/${categoryName}`;
//     })
//     .catch(error => {
//         console.error('Ошибка:', error);
//     });
// };