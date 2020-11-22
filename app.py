from flask import Flask, render_template, request
from werkzeug import secure_filename
import os
import sys
import socket

FILENAME = 'config.cfg'
UPLOAD_FOLDER = '/home/www/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.filename = FILENAME
        if f:
            filename = secure_filename(f.filename)
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('success.html')
    return render_template('failure.html')

if __name__ == '__main__':
    h_name = socket.gethostname()
    ip_addres = socket.gethostbyname(h_name)
    app.run(debug=True, port=80, host=ip_addres)