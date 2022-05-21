from flask import Flask
import flask_restful as restful

app = Flask(__name__)
api = restful.Api(app, prefix='/rms/v1/')

# Service Layer Imports
from rms.controller.http.food import Food
from rms.controller.http.order import Order
from rms.controller.http.cart import Cart
from rms.controller.http.customer import Customer

# End Points
api.add_resource(Food, 'food/', 'food/<string:id>')
api.add_resource(Order, 'order/', 'order<string:id>')
api.add_resource(Cart, 'cart/', 'cart/<string:id>')
api.add_resource(Customer, 'customer/', 'customer/<string:id>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4331, debug=True)
