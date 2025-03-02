-- Пример запроса для поиска
SELECT * FROM products
WHERE to_tsvector('english', name) @@ to_tsquery('english', 'название_товара');

--   ========================= Схема DWР =========================
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    date_inserted TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price NUMERIC(10, 2) NOT NULL,
    category_id INT REFERENCES categories(category_id),
    image VARCHAR(255) DEFAULT 'test_path',
    date_inserted TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- Индекс для поиска на английском языке
CREATE INDEX idx_products_name ON products USING gin (to_tsvector('english', name));

CREATE TABLE attributes (
    attribute_id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);


CREATE TABLE product_attributes (
    product_id INTEGER REFERENCES products(product_id),
    attribute_id INTEGER REFERENCES attributes(attribute_id),
    value VARCHAR(100) NOT NULL,
    PRIMARY KEY (product_id, attribute_id)
);


CREATE TABLE inventory (
    inventory_id INTEGER PRIMARY KEY,
    product_id INTEGER REFERENCES products(product_id),
    quantity INTEGER NOT NULL,
    location VARCHAR(255)
);


CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount NUMERIC(10, 2) NOT NULL
);


CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(order_id),
    product_id INTEGER REFERENCES products(product_id),
    quantity INTEGER NOT NULL,
    price NUMERIC(10, 2) NOT NULL
);


CREATE TABLE carts (
    user_id INTEGER REFERENCES users(user_id),
    product_id INTEGER REFERENCES products(product_id),
    quantity INTEGER NOT NULL,
    date_time_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE UNIQUE INDEX idx_carts_user_product ON carts(user_id, product_id);
