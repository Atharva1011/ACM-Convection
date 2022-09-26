from flask import Flask, flash, request, redirect, url_for, render_template, Blueprint
import urllib.request
import os
from . import ml_model
from werkzeug.utils import secure_filename
from PIL import Image


UPLOAD_FOLDER = 'static/uploads/'

uploads = Blueprint('uploads', __name__)

# app.secret_key = "secret key"
# uploads.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# uploads.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024



ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@uploads.route('/upload')
def home():
    return render_template('uploads.html')

@uploads.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        image = Image.open(file)
        # Get the current working directory
        cwd = os.path.dirname(os.path.abspath(__file__))

        file_path=os.path.join(cwd,UPLOAD_FOLDER,filename)
        # print(file_path)
        resized_img = image.resize((400, 400))
        resized_img.save(file_path)
        
        food_name=ml_model.food_identifier(file_path)
        print(food_name)
        # return render_template("result.html", result=food_name)
        return render_template('uploads.html', filename=filename, food=food_name)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)

@uploads.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)
