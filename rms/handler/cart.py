from bson import ObjectId

from rms.dao.cart import clear_product_in_cart, get_cart_by_customer_id, get_cart_by_id, \
    add_product_in_cart, add_new_cart
from rms.dao.food import get_food_by_id
from rms.dao.order import create_new_order
from rms.views.cart import single


def patch_handler(cart_id, action, body):
    if action == "ADD_ITEM":
        food_item_id_count_map = {item["id"]: item["quantity"] for item in body}
        add_product_in_cart(cart_id, food_item_id_count_map)

    if action == "CHECKOUT":
        cart = get_cart_by_id(cart_id)

        payment_mode = body["mode"]
        payment_status = "PAID" if body["mode"] == "DIGITAL" else "UNPAID"
        food_list = cart["foodList"]
        bill_amount = 0.0
        customer_id = cart["customerId"]

        for item in food_list:
            item_price = get_food_by_id(ObjectId(item["id"]))["price"]
            bill_amount += item_price*item["quantity"]

        create_new_order(
            customer_id, bill_amount,
            payment_status,
            payment_mode
        )

        clear_product_in_cart(cart_id)

    cart = get_cart_by_id(cart_id)

    return single(cart)


def get_cart_handler(cart_id, customer_id=None):
    if customer_id:
        cart = get_cart_by_id(cart_id)
    else:
        cart = get_cart_by_customer_id(customer_id)
    return single(cart)


def add_new_cart_handler(customer_id):
    new_cart_object_id = add_new_cart(customer_id)
    new_cart = get_cart_by_id(new_cart_object_id)

    return single(new_cart)

