import flask_restful as restful


class Customer(restful.Resource):
    def post(self):
        return {"status": 200}

    def patch(self, id):
        if id:
            return {"status": 200}

        return {"status": 401}

    def get(self, id):
        if id:
            return {"status": 200}

        return {"status": 401}
