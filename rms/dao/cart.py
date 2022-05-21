from bson import ObjectId
from pymongo import ReturnDocument

from configs.settings import mongo_client
cart_collection = mongo_client['rms']['cart']

from rms.utils.datetime_operation import get_current_datetime


def default_doc_struct_of_cart(customer_id):
    return {
        "foodList": [],
        "customerId": customer_id,
        "lastUpdatedAt": None,
        "createdAt": get_current_datetime()
    }


def add_new_cart(customer_id):
    new_cart = default_doc_struct_of_cart(customer_id)
    return cart_collection.insert(new_cart)


def get_cart_by_id(cart_id):
    """
    :param cart_id: ObjectId
    :return: cursor object
    """
    return cart_collection.find_one({
        "_id": ObjectId(cart_id)
    })


def get_cart_by_customer_id(customer_id):
    """
    :param custmer_id: ObjectId
    :return: cursor object
    """

    return cart_collection.find_one({
        "_id": ObjectId(customer_id)
    })


def add_product_in_cart(cart_id, foodlist):
    """
    :param cart_id: ObjectId
    :param productlist: dict of structure like
    {id:1, id:2}
    :return: cursor object
    """

    prev_record = cart_collection.find({
        "_id": ObjectId(cart_id)
    })
    food_list = []
    if prev_record:
        food_list = prev_record["foodList"]

        for food in food_list:
            if food["id"] in foodlist:
                food["quantity"] = foodlist[food["id"]]
    else:
        for id in foodlist:
            food_list[id] = foodlist[id]

    return cart_collection.find_one_and_update(
        {
            "_id": ObjectId(cart_id)
        },
        {
            "$set": {
                "foodList": food_list,
                "lastUpdatedAt": get_current_datetime()
            }
        },
        upsert=True,
        return_document=ReturnDocument.AFTER
    )


def clear_product_in_cart(cart_id):
    """
        :param cart_id: ObjectId
        :param productlist: dict of structure like
        [{
            "productId": id,
            "quantity": 1
        }]
        :return: cursor object
        """

    return cart_collection.find_one_and_update(
        {
            "_id": ObjectId(cart_id)
        },
        {
            "$set": {
                "foodList": [],
                "lastUpdatedAt": get_current_datetime()
            }
        },
        upsert=True,
        return_document=ReturnDocument.AFTER
    )
