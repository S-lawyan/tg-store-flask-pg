INSERT INTO categories (category_id, name)
VALUES
(1, 'Смартфоны'),
(2, 'Ноутбуки'),
(3, 'Телевизоры'),
(4, 'Аксессуары');


INSERT INTO products (product_id, name, description, price, category_id, image, image_mime_type)
VALUES
-- Телефоны (20 строк)
(1, 'iPhone 14', 'Смартфон Apple с OLED-дисплеем', 999.99, 1, NULL, NULL),
(2, 'Samsung Galaxy S22', 'Флагманский смартфон Samsung', 899.99, 1, NULL, NULL),
(3, 'Google Pixel 7', 'Смартфон с чистой Android', 799.99, 1, NULL, NULL),
(4, 'OnePlus 10 Pro', 'Смартфон с быстрой зарядкой', 749.99, 1, NULL, NULL),
(5, 'Xiaomi 12', 'Смартфон с AMOLED-дисплеем', 699.99, 1, NULL, NULL),
(6, 'iPhone 13', 'Предыдущая модель iPhone', 799.99, 1, NULL, NULL),
(7, 'Samsung Galaxy A53', 'Бюджетный смартфон Samsung', 399.99, 1, NULL, NULL),
(8, 'Google Pixel 6a', 'Доступный смартфон от Google', 449.99, 1, NULL, NULL),
(9, 'OnePlus Nord 2', 'Смартфон среднего уровня', 499.99, 1, NULL, NULL),
(10, 'Xiaomi Redmi Note 11', 'Бюджетный смартфон', 299.99, 1, NULL, NULL),
(11, 'iPhone SE 2022', 'Компактный iPhone', 429.99, 1, NULL, NULL),
(12, 'Samsung Galaxy Z Flip4', 'Складной смартфон', 999.99, 1, NULL, NULL),
(13, 'Google Pixel 5a', 'Смартфон с отличной камерой', 499.99, 1, NULL, NULL),
(14, 'OnePlus 9', 'Флагманский смартфон', 699.99, 1, NULL, NULL),
(15, 'Xiaomi Mi 11', 'Смартфон с высоким разрешением экрана', 599.99, 1, NULL, NULL),
(16, 'iPhone 12', 'Популярная модель iPhone', 699.99, 1, NULL, NULL),
(17, 'Samsung Galaxy S21 FE', 'Фанатовская версия S21', 599.99, 1, NULL, NULL),
(18, 'Google Pixel 4a', 'Компактный смартфон', 349.99, 1, NULL, NULL),
(19, 'OnePlus 8T', 'Смартфон с быстрой зарядкой', 549.99, 1, NULL, NULL),
(20, 'Xiaomi Poco X4 Pro', 'Смартфон для геймеров', 399.99, 1, NULL, NULL),

-- Ноутбуки (10 строк)
(21, 'MacBook Air M2', 'Ультратонкий ноутбук Apple', 1199.99, 2, NULL, NULL),
(22, 'Dell XPS 13', 'Премиальный ноутбук Dell', 1299.99, 2, NULL, NULL),
(23, 'HP Spectre x360', 'Ноутбук-трансформер', 1099.99, 2, NULL, NULL),
(24, 'Lenovo ThinkPad X1 Carbon', 'Бизнес-ноутбук', 1399.99, 2, NULL, NULL),
(25, 'Asus ROG Zephyrus G14', 'Игровой ноутбук', 1499.99, 2, NULL, NULL),
(26, 'Acer Swift 3', 'Бюджетный ноутбук', 699.99, 2, NULL, NULL),
(27, 'Microsoft Surface Laptop 4', 'Ноутбук от Microsoft', 1299.99, 2, NULL, NULL),
(28, 'Razer Blade 15', 'Игровой ноутбук', 1999.99, 2, NULL, NULL),
(29, 'LG Gram 17', 'Легкий ноутбук', 1499.99, 2, NULL, NULL),
(30, 'MSI Prestige 14', 'Ноутбук для творчества', 1199.99, 2, NULL, NULL),

-- Телевизоры (5 строк)
(31, 'Samsung QLED Q80A', 'Телевизор с технологией QLED', 1499.99, 3, NULL, NULL),
(32, 'LG OLED C1', 'Телевизор с OLED-дисплеем', 1799.99, 3, NULL, NULL),
(33, 'Sony Bravia XR A80J', 'Телевизор с процессором Cognitive Processor XR', 1999.99, 3, NULL, NULL),
(34, 'TCL 6-Series', 'Телевизор с Mini-LED подсветкой', 999.99, 3, NULL, NULL),
(35, 'Hisense U8G', 'Телевизор с Quantum Dot технологией', 899.99, 3, NULL, NULL),

-- Аксессуары (5 строк)
(36, 'Case for iPhone 14', 'Защитный чехол', 19.99, 4, NULL, NULL),
(37, 'Case for Samsung Galaxy S22', 'Силиконовый чехол', 14.99, 4, NULL, NULL),
(38, 'B-C Cable', 'Кабель для зарядки', 9.99, 4, NULL, NULL),
(39, 'Wireless charging', 'Зарядная станция Qi', 29.99, 4, NULL, NULL),
(40, 'Earpods Pro Headphones', 'Беспроводные наушники', 249.99, 4, NULL, NULL);
