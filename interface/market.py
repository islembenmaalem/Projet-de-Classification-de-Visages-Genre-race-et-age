import matplotlib.pyplot as plt
import cv2
from flask import Flask, render_template, request, url_for, flash, redirect
from fileinput import filename
from flask import jsonify
#from distutils.log import debug
import os
from flask import Flask, render_template
from tensorflow.keras.utils import load_img
from flask_cors import CORS
import sys
import tensorflow as tf
from PIL import Image
import numpy as np
static_path="C:/Users/MSI/Downloads/projet deep/proj deep/mini projet 2/apps/static/"

# prolly prob somewherepip3 uninstall flask_cors
# initialisation built in var refer to local python file
app = Flask(__name__)
CORS(app)
# decorator : one step a function before excuted ,
# root url

# set FLASK_APP=market.py
# http://127.0.0.1:5000/0
# set FLASK_DEBUG=1
# awka tsava good now see
# open any php project one minute code?

# @app.route('/')
# def hello_world():
#   return '<h1>hello world with debug<h1>'

# http://127.0.0.1:5000/about

# @app.route('/about')
# def about_page():
# return '<h1>this is the abt page of </h1>'

# http://127.0.0.1:5000/about/sahar
# <username> accept any var there
#CORS(app, resources={r"/api/*": {"origins": "*"}})


# @app.route('/about/<username>')
# def about_page(username):
# return f'<h1>this is the abt page of {username}</h1>'

# we create templates and refer our routes to those diff htmls


# py -m venv .env
# .env\scripts\activate
# pip install -r req.txt
app = Flask(__name__)


@app.route('/')
# @cross_origin()
def main():
    return render_template("index.html")


PEOPLE_FOLDER = os.path.join('static')

app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

# yes but you need to find solution for cors with this fucking python
# it works only in your pc like this
# but as you see it's simple php to pythonyeeee got the whole struture thank _u a lot
# you are welcome , amma go sleep T_T, see u tmr ?? yes see me tomorrow BAHI MELAAAAAA THANK YA AGAINGo to sleep ok ok


@app.route('/success', methods=['GET', 'POST'])
def success():
    
    model = tf.keras.models.load_model('model_cnn_10000_2l.h5')
    if request.method == 'POST':
        uploads_dir = os.path.join("./")
        f = request.files['file']
        if (f.filename):
            # save
            print("/static/"+f.filename)
            f.save(os.path.join(uploads_dir,f.filename))
            #f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
            full_filename = os.path.join(
                app.config['UPLOAD_FOLDER'], f.filename)
            #full_filename ="/static/"+f.filename
            #plt.imsave("/.static",f.filename)
            img = load_img(f.filename, grayscale=True)
            img1=plt.imread(f.filename)
            img = img.resize((128, 128), Image.ANTIALIAS)
            img = np.array(img)
            pred = model.predict(img.reshape(1, 128, 128, 1))
            genre=round(pred[0][0][0])
            age=round(pred[1][0][0])
            race=round(pred[2][0][0])
            print(genre,age,race)
            match genre:
                case 0:
                    genre="Male"
                case _:
                    genre="Female"
            match race:
                case 0:
                    race="White"
            #    case 1:
                #    race="Black"
                case 2:
                    race="Asian"
                case 3:
                    race="Indian"
                case _:
                    race="others"
            #originalmage=plt.imread(f.filename)

            plt.imsave(static_path+f.filename,img1)
                
            
           # return jsonify(filename=f.filename,
           #                full_filename=full_filename
           #                )
            
            return render_template("success.html", name=f.filename,genre=genre,age=age,race=race,user_image=full_filename)
        else:
            return jsonify(error="file not found")
    else:
        # return render_template("index.html")
        return jsonify(error="GET method not allowed")
if __name__=="__main__":
    app.run(port=5000,debug=True)