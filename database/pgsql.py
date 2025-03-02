from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    date_inserted = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=False)

    # relationships
    orders = db.relationship('Orders', back_populates='users')
    carts = db.relationship('Carts', back_populates='users')


class Categories(db.Model):
    __tablename__ = 'categories'
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    # relationships
    product = db.relationship('Products', back_populates='categories')


class Products(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    description = db.Column(db.String(100), unique=False, nullable=True)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'), nullable=True)
    image = db.Column(db.String(255), default="test_path")
    date_inserted = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=False)
    updated_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=False)

    # relationships
    categories = db.relationship('Categories', back_populates='product')
    attributes = db.relationship('ProductAttributes', back_populates='product')
    inventory = db.relationship('Inventory', back_populates='product')
    order_items = db.relationship('OrderItems', back_populates='product')
    carts = db.relationship('Carts', back_populates='product')


class Attributes(db.Model):
    __tablename__ = 'attributes'
    attribute_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # relationships
    products_attributes = db.relationship('ProductAttributes', back_populates='attributes')


class ProductAttributes(db.Model):
    __tablename__ = 'product_attributes'
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), primary_key=True)
    attribute_id = db.Column(db.Integer, db.ForeignKey('attributes.attribute_id'), primary_key=True)
    value = db.Column(db.String(100), nullable=False)

    # relationships
    product = db.relationship('Products', back_populates='attributes')
    attributes = db.relationship('Attributes', back_populates='products_attributes')


class Inventory(db.Model):
    __tablename__ = 'inventory'
    inventory_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    quantity = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(255), nullable=False)

    # relationships
    product = db.relationship('Products', back_populates='inventory')


class Orders(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    order_date = db.Column(db.TIMESTAMP, nullable=False)
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)

    # relationships
    # product = db.relationship('Products', back_populates='orders')
    users = db.relationship('Users', back_populates='orders')
    order_items = db.relationship('OrderItems', back_populates='order')


class OrderItems(db.Model):
    __tablename__ = 'order_items'
    order_item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

    # relationships
    order = db.relationship('Orders', back_populates='order_items')
    product = db.relationship('Products', back_populates='order_items')


class Carts(db.Model):
    __tablename__ = 'carts'
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'))
    quantity = db.Column(db.Integer, nullable=False)
    date_time_added = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=False)

    # relationships
    users = db.relationship('Users', back_populates='carts')
    product = db.relationship('Products', back_populates='carts')


__all__ = [
    "Users",
    "Products",
    "Categories",
    "Inventory",
    "Attributes",
    "ProductAttributes",
    "Orders",
    "OrderItems",
    "db"
]



