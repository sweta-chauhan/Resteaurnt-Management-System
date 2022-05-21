from rms.utils.datetime_operation import get_current_datetime_in_str


def single(order):
    return {
        "customerId": str(order["customerId"]),
        "status": order["status"],
        "createdAt": get_current_datetime_in_str(order["createdAt"]),
        "modifiedAt": get_current_datetime_in_str(order["modifiedAt"]),
        "billAmount": order["billAmount"],
        "paymentStatus": order["paymentStatus"],
        "mode": order["mode"]
    }