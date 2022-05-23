from flask.globals import request
import flask_restful as restful

from rms.handler.food import get_all_food_for_customer, update_food_handler, add_new_food


class Food(restful.Resource):
    def post(self):
        request_data = request.get_json(force=True)
        name = request_data.get("name")
        category = request_data.get("category")
        timeslot = request_data.get("timeslot")
        price = float(request_data.get("price", 0))
        in_stock = request_data.get("in_stock") == 'true'

        resp = add_new_food(name, category, timeslot, price, in_stock)

        return {"status": 200, "result": resp}

    def patch(self, id=None):
        param_json = request.args.to_dict()
        status = param_json.get('status') == 'true'
        if id:
            resp = update_food_handler(id, status)

            return {"status": 200, "result": resp}

        return {"status": 401}

    def get(self, id=None):
        param_json = request.args.to_dict()
        slot = param_json.get('slot')
        food_type = param_json.get('foodType')

        if not id:
            resp = get_all_food_for_customer(slot, food_type)
            return {"status": 200, "results": resp}

        return {"status": 401}

