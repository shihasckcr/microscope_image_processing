from flask import Flask, request, render_template, send_file
import cv2
import os
import numpy as np
from utils.stitching import stitch_images
from utils.roi import select_roi
from utils.zoom import zoom_image
from utils.auto_focus import auto_focus

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('images')
    for file in files:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return "Images uploaded successfully."

@app.route('/stitch_images')
def stitch():
    img_paths = [os.path.join(UPLOAD_FOLDER, img) for img in os.listdir(UPLOAD_FOLDER)]
    result_path = 'results/stitched_result.jpg'
    stitch_images(img_paths, result_path)
    return send_file(result_path, as_attachment=True)

@app.route('/roi_selection', methods=['POST'])
def roi():
    x = int(request.form['x'])
    y = int(request.form['y'])
    width = int(request.form['width'])
    height = int(request.form['height'])
    
    img_path = os.path.join(UPLOAD_FOLDER, os.listdir(UPLOAD_FOLDER)[0])
    result_path = 'results/roi_result.jpg'
    select_roi(img_path, x, y, width, height, result_path)
    
    return send_file(result_path, as_attachment=True)

@app.route('/zoom', methods=['POST'])
def zoom():
    zoom_factor = float(request.form['zoom_factor'])
    
    img_path = os.path.join(UPLOAD_FOLDER, os.listdir(UPLOAD_FOLDER)[0])
    result_path = 'results/zoomed_result.jpg'
    zoom_image(img_path, zoom_factor, result_path)
    
    return send_file(result_path, as_attachment=True)

@app.route('/auto_focus')
def autofocus():
    img_path = os.path.join(UPLOAD_FOLDER, os.listdir(UPLOAD_FOLDER)[0])
    result_path = 'results/auto_focus_result.jpg'
    auto_focus(img_path, result_path)
    return send_file(result_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
