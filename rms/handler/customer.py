from rms.dao.customer import add_customer, update_customer, get_customer_by_id
from rms.views.customer import single


def add_new_customer_handler(name, phone_number):
    new_customer = add_customer(name, phone_number)
    new_customer = get_customer_by_id(new_customer["_id"])
    return single(new_customer)


def update_customer_handler(id, name=None, phone_number=None):
    customer = update_customer(id, name, phone_number)
    return single(customer)
