from flask import Flask, render_template, request, Response
import requests
from VisualizeResults import *
import json
# from chat import bott

app=Flask(__name__)

@app.route('/')
def hello():
  img_file=['test/Brats18_2013_2_1_t2.nii.gz',
  'test/Brats18_2013_2_1_t1ce.nii.gz']
  op_img(img_file)
  return render_template('bot.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      return 'file uploaded successfully'

if __name__ == '__main__':
   app.run(debug = True)
