from flask import Flask, request, jsonify
from .model import Script
from .session import Session # Connect to the database

app = Flask(__name__)


@app.route("/create", methods=["POST"])
def create_script():
    script = Script()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)