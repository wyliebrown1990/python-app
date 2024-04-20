from flask import Flask, jsonify
app = Flask(__name__)

# Dummy data
products = {
    1: {"name": "Laptop", "price": 800},
    2: {"name": "Smartphone", "price": 500}
}

@app.route('/products/<int:product_id>')
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
