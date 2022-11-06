from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    data = {
        "name": "Yae",
        "age": 32,
        "message": "Hello API"
        }
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
