from rms.utils.datetime_operation import get_current_datetime_in_str


def single(cart):
    return {
        "foodList": cart["foodList"],
        "customerId": cart["customerId"],
        "lastUpdatedAt": get_current_datetime_in_str(cart["lastUpdatedAt"]),
        "createdAt": get_current_datetime_in_str(cart["createdAt"]),
        "cartId": str(cart["_id"])
    }


def multiple(carts):
    return [single(cart) for cart in carts]