from rms.dao.food import get_all_food, add_food, get_food_by_id, update_food_status
from rms.views.food import multiple, single


def get_all_food_for_customer(slot, food_type):
    food_list = get_all_food(time_slot=slot, category=food_type)
    return multiple(food_list)


def add_new_food(name, category, timeslot, price, in_stock):
    food_object_id = add_food(name, category, timeslot, price, in_stock)
    food = get_food_by_id(food_object_id)
    return single(food)


def update_food_handler(id, status):
    food = update_food_status(id, in_stock=status)
    return single(food)