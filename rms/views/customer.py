from rms.utils.datetime_operation import get_current_datetime_in_str

def single(customer):
    return {
        "firstName": customer["customer"],
        "phoneNumer": customer["phoneNumber"],
        "createdAt": get_current_datetime_in_str(customer["createdAt"])
    }