#!/usr/bin/env python
import random
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data
orders = {}
order_id = 1  # to keep track of the next order ID

@app.route('/orders/<int:order_id>')
def get_order(order_id):
    order = orders.get(order_id)
    if order:
        return jsonify(order)
    else:
        return jsonify({"error": "Order not found"}), 404

@app.route('/purchase', methods=['POST'])
def purchase_product():
    global order_id
    user_id = request.json.get('user_id')
    product_id = request.json.get('product_id')
    price = random.randint(1, 20)  # generate a random price between $1 and $20

    # Creating a new order
    new_order = {
        "user_id": user_id,
        "product_ids": [product_id],
        "price": price
    }
    orders[order_id] = new_order
    response = jsonify(new_order)
    response.status_code = 201
    order_id += 1
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
