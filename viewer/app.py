#!/usr/bin/env python3
import os
from flask import Flask, render_template, send_from_directory

__author__ = 'aryehzapinsky'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Used gallery presented in link as starting point:
# https://github.com/ibrahimokdadov/upload_file_python/blob/master/src/app_display_multiple_images.py
@app.route('/gallery/<filename>')
def send_image(filename):
    return send_from_directory("summary_images", filename)

# Used gallery presented in link as starting point:
# https://github.com/ibrahimokdadov/upload_file_python/blob/master/src/app_display_multiple_images.py
@app.route('/gallery')
def get_gallery():
    image_names = sorted(os.listdir('./summary_images'))
    print(image_names)
    return render_template("gallery.html", image_names=image_names)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4555, debug=True)
