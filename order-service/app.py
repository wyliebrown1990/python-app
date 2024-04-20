from flask import Flask, jsonify
app = Flask(__name__)

# Dummy data
orders = {
    1: {"user_id": 1, "product_ids": [1, 2]},
    2: {"user_id": 2, "product_ids": [2]}
}

@app.route('/orders/<int:order_id>')
def get_order(order_id):
    order = orders.get(order_id)
    if order:
        return jsonify(order)
    else:
        return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
