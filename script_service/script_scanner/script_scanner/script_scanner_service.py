from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/")
def scan():
    return("<h1>Script Scanner Service</h1><p>This site is a prototype API for scanning scripts.</p>")

@app.route("/scan", methods=["POST"])
def scan_script():
    data = request.get_json()
    return data


if __name__=="__main__":
    print("Script Scanner Service is running")
    app.run(debug=True, port=5000, host='0.0.0.0')