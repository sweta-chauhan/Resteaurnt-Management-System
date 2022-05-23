from bson import ObjectId
from pymongo import ReturnDocument

from rms.utils.datetime_operation import get_current_datetime

from configs.settings import mongo_client
order_collection = mongo_client['rms']['order']


def default_structure_of_order_doc(id, bill_amount, payment_status, mode):
    return {
        "customerId": id,
        "status": "PENDING",
        "createdAt": get_current_datetime(),
        "modifiedAt": None,
        "billAmount": bill_amount,
        "paymentStatus": payment_status,
        "mode": mode,
    }


def create_new_order(id, bill_amount, payment_status, mode):
    new_order = default_structure_of_order_doc(id, bill_amount, payment_status, mode)
    return order_collection.insert(new_order)


def update_order_status(id, status):
    return order_collection.find_one_and_update(
            {
                "_id": ObjectId(id)
            },
            {
                "$set": {
                    "status": status,
                    "modifiedAt": get_current_datetime()
                }
            },
        upsert=True,
        return_document=ReturnDocument.AFTER
    )
