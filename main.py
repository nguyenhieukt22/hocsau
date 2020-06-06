from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import json
import cv2, os
from Model import model,date
app = Flask(__name__)
@app.route('/')
def index():
   return render_template('index.html')
@app.route('/uploade', methods=['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
      f = request.files['inputImg']
      f.save('static/%s' %(f.filename))
      name=f.filename
      resul = 'static/%s' %(f.filename)
      predict="29-S6 81223 "
      return render_template('result.html', img =resul, predict=predict, img_dect=resul)
if __name__ == '__main__':
   app.run(debug = True)