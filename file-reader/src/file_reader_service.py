from flask import Flask, request, jsonify

app = Flask(__name__)

# @app.route('/read', methods=['POST'])
# def read_file():
#     data = request.get_json()
#     file_path = data['file_path']
#     # Read file and extract raw content
#     with open(file_path, 'r') as file:
#         raw_content = file.read()
#     # Initialize Script object
#     script = {
#         'raw_content': raw_content
#     }
#     return jsonify(script)

@app.route("/")
def home():
    return("<h1>File Reader Service</h1><p>This site is a prototype API for reading files.</p>")

@app.route("/read", methods=["POST"])
def read_file():
    data = request.get_json()
    return data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)