from rms.dao.order import update_order_status
from rms.views.order import single


def patch_order_status(id,status):
    order = update_order_status(id, status)
    return single(order)
