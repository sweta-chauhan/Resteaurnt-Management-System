from flask.globals import request
import flask_restful as restful

from rms.handler.order import patch_order_status


class Order(restful.Resource):
    def patch(self, id):
        param_json = request.args.to_dict()
        status = param_json.get('status')
        if id:
            resp = patch_order_status(id, status)
            return {"status": 200, "result": resp}

        return {"status": 401}
