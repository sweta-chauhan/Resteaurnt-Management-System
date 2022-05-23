from flask.globals import request
import flask_restful as restful

from rms.handler.customer import add_new_customer_handler, update_customer_handler


class Customer(restful.Resource):
    def post(self):
        request_data = request.get_json(force=True)
        name = request_data.get("name")
        phone_number = request_data.get("phoneNumber")
        response = add_new_customer_handler(name, phone_number)

        return {"status": 200, "result": response}

    def patch(self, id=None):
        param_json = request.args.to_dict()
        name = param_json.get("name")
        phone_number = param_json.get("phoneNumber")

        if id:
            resp = update_customer_handler(id, name, phone_number)
            return {"status": 200, "result": resp}

        return {"status": 401}

    def get(self, id=None):
        if id:
            return {"status": 200}

        return {"status": 401}
