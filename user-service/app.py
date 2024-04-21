#!/usr/bin/env python
from flask import Flask, jsonify
app = Flask(__name__)

# Dummy data
users = {
    1: {"name": "Alice", "age": 30},
    2: {"name": "Bob", "age": 24}
}

@app.route('/users/<int:user_id>')
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
