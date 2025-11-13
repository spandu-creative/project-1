from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("🔔 Received Alert:", data)
    return jsonify({"status": "received"}), 200

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Webhook endpoint is active!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
