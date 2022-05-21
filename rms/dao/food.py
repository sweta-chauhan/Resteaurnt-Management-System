from bson import ObjectId
from pymongo import ReturnDocument

from configs.settings import mongo_client
food_collection = mongo_client['rms']['food']


def default_structure_of_food_doc(name, category, timeslot, price, in_stock=False):

    return {
        "name": name,
        "category": category,
        "slot": timeslot,
        "inStock": in_stock,
        "price": price
    }


def add_food(name, category, timeslot, price, in_stock):
    new_food_item = default_structure_of_food_doc(name, category, timeslot, price, in_stock)
    return food_collection.insert(new_food_item)


def update_food_status(id, in_stock=False):
    return food_collection.find_one_and_update(
            {
                "_id": ObjectId(id)
            },
            {
                "$set": {
                    "inStock": in_stock
                }
            },
        upsert=False,
        return_document=ReturnDocument.AFTER
    )


def get_all_food(time_slot, category):
    return food_collection.find({
        "timeSlot": time_slot,
        "category": category
    })


def get_food_by_id(id):
    return food_collection.find({"_id": ObjectId(id)})

