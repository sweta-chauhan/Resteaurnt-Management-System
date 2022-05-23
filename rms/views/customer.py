from rms.utils.datetime_operation import get_current_datetime_in_str


def single(customer):
    return {
        "firstName": customer["firstName"],
        "phoneNumer": customer["phoneNumer"],
        "createdAt": get_current_datetime_in_str(customer["createdAt"]),
        "customerId": str(customer["_id"])
    }