from flask import Flask, request, jsonify

app = Flask(__name__)

# Временная «база данных» в памяти
users = []

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"error": "Invalid data"}), 400

    user = {
        "id": len(users) + 1,
        "name": data['name']
    }
    users.append(user)
    return jsonify(user), 201

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return jsonify({"message": "Deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)