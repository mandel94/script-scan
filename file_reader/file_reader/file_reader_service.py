from flask import Flask, request, jsonify

app = Flask(__name__)


def read_file(file_path):
    # Read file and extract raw content
    with open(file_path, 'r') as file:
        raw_content = file.read()
    # Import Script from domain model
    return raw_content


@app.route("/read", methods=["POST"])
def read_file_wrapper():
    script = read_file(request.get_json()["file_path"])



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)