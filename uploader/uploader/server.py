from flask import Flask, request, jsonify, flash, redirect, url_for, send_from_directory, render_template, abort
import os
from werkzeug.utils import secure_filename

# https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/
# https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask

# The idea is to create a service that allows to upload files to a specific remote folder. 

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = [".txt", ".html", ".pdf"]
app.config['UPLOAD_PATH'] = 'uploads' # Load to a remote server that is accessible by the all services



@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html', files=files)

@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return redirect(url_for('index'))


if __name__=="__main__":
    print("Uploader Service is running")
    app.run(debug=True, port=5000, host='0.0.0.0')