from flask import Blueprint
from flask import request
from flask import jsonify
from flask import render_template
from sqlalchemy.sql import text
from database.pgsql import db
from database.pgsql import Products, Categories, Carts
from urllib.parse import unquote
from loguru import logger

"""
    This file contains the client routes, which are accessible to all users (clients).
"""

client_bp = Blueprint("client_bp", __name__)


@client_bp.route('/')
def hello_world():
    user_id = 123456789
    products: list[Products] = db.session.query(Products).join(Categories, Products.category_id == Categories.category_id).all()
    categories: list[Categories] = db.session.query(Categories).all()
    user_cart: list[Carts] = db.session.query(Carts.product_id, Carts.quantity).filter(Carts.user_id == user_id).all()
    cart = {item.product_id: item.quantity for item in user_cart}

    return render_template("index.html", products=products, categories=categories, cart=cart, category_name="Все товары")


@client_bp.route('/category/<category_name>')
def category(category_name: str):
    user_id = 123456789
    _category_name = unquote(category_name)
    products: list[Products] = db.session.query(Products)\
        .join(Categories, Products.category_id == Categories.category_id)\
        .filter(Categories.name == _category_name).all()
    categories: list[Categories] = db.session.query(Categories).all()
    user_cart: list[Carts] = db.session.query(Carts.product_id, Carts.quantity).filter(Carts.user_id == user_id).all()
    cart = {item.product_id: item.quantity for item in user_cart}

    return render_template("index.html", products=products, categories=categories, cart=cart, category_name=_category_name)


@client_bp.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    user_id: int = int(request.form.get('user_id'))
    product_id: int = int(request.form.get('product_id'))
    quantity: int = int(request.form.get('quantity'))
    # TODO ошибка добавления непонятная
    try:

        db.session.execute(
            text(f"""
                INSERT INTO carts (user_id, product_id, quantity, date_time_added) 
                VALUES ({user_id}, {product_id}, {quantity}, CURRENT_TIMESTAMP)
                ON CONFLICT (user_id, product_id)
                DO UPDATE SET
                    quantity = EXCLUDED.quantity,
                    date_time_added = CURRENT_TIMESTAMP;
            """)
        )
        db.session.commit()
        logger.info(f"Product {product_id} ({quantity}) added to basket user №{user_id}")
        return jsonify({"success": True})
    except Exception as exc:
        db.session.rollback()
        logger.error(f"Error adding product to basket:\n {exc}")
        return jsonify({"success": False, "error": str(exc)})


@client_bp.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    user_id = request.form.get('user_id')
    product_id = request.form.get('product_id')

    try:
        db.session.query(Carts).filter(Carts.user_id == user_id, Carts.product_id == product_id).delete()
        db.session.commit()
        logger.info(f"Product {product_id} remove from basket user №{user_id}")
        return jsonify({"success": True})
    except Exception as exc:
        db.session.rollback()
        logger.error(f"Error removing product from basket:\n {exc}")
        return jsonify({"success": False, "error": str(exc)})

