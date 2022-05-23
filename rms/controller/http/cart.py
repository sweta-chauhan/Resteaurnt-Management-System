import flask_restful as restful
from flask.globals import request

from rms.handler.cart import get_cart_handler, patch_handler, add_new_cart_handler


class Cart(restful.Resource):
    def post(self):
        request_data = request.get_json(force=True)
        customer_id = request_data.get("customerId")
        resp = add_new_cart_handler(customer_id)
        return {"status": 200, "result": resp}

    def patch(self, id=None):
        request_data = request.get_json(force=True)
        action = request_data.get("action")
        body = request_data.get("body")
        if id:
            resp = patch_handler(
                cart_id=id,
                action=action,
                body=body
            )

            return {"status": 200, "result": resp}

        return {"status": 401}

    def get(self, id=None):
        param_json = request.args.to_dict()
        customer_id = param_json.get("customerId")

        if id:
            resp = get_cart_handler(cart_id=id)
            return {"status": 200, "result": resp}
        if customer_id:
            resp = get_cart_handler(
                cart_id=id,
                customer_id=customer_id
            )
            return {"status": 200, "result": resp}

        return {"status": 401}

