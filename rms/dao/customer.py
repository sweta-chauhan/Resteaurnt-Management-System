from bson import ObjectId
from pymongo import ReturnDocument

from rms.utils.datetime_operation import get_current_datetime

from configs.settings import mongo_client
customer_collection = mongo_client['rms']['customer']


def default_structure_of_customer_doc(name, phone_number):
    return {
        "firstName": name,
        "phoneNumer": phone_number,
        "createdAt": get_current_datetime()
    }


def add_customer(name, phone_number):
    new_customer = default_structure_of_customer_doc(name, phone_number)
    return customer_collection.insert(new_customer)


def update_customer(id, name=None, phone_number=None):
    update_dict = {}

    if name:
        update_dict["name"] = name

    if phone_number:
        update_dict["phoneNumber"] = phone_number

    if update_dict:
        return customer_collection.find_one_and_update(
            {
                "_id": ObjectId(id)
            },
            {
                "$set": update_dict
            },
            upsert=True,
            return_document=ReturnDocument.AFTER
        )


def get_customer_by_id(id):
    return customer_collection.find_one({
        "_id": ObjectId(id)
    })
