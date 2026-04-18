import psutil
from flask import Flask, jsonify

app = Flask(__name__)
process = psutil.Process()

@app.route("/")
def home():
    return jsonify({"message": "API is running"}), 200

@app.route("/health")
def health():
    cpu_usage = f"{psutil.cpu_percent(interval=0.1):.2f}%"
    memory_usage = f"{process.memory_info().rss / (1024 * 1024):.2f}MB"

    return jsonify({
        "message": "healthy",
        "cpu": cpu_usage,
        "memory": memory_usage
    }), 200

@app.route("/me")
def me():
    return jsonify({
        "name": "Damilare Idowu",
        "email": "aideedrey@gmail.com",
        "github": "https://github.com/Dreybest/hng-stage1"
    }), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
