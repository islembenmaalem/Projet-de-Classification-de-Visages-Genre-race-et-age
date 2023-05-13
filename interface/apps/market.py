import matplotlib.pyplot as plt
import cv2
from flask import Flask, render_template, request, url_for, flash, redirect
from fileinput import filename
from flask import jsonify
#from distutils.log import debug
import os
from flask import Flask, render_template
from flask_cors import CORS
import sys

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
    if request.method == 'POST':
        uploads_dir = os.path.join("./")
        f = request.files['file']
        if (f.filename):
            # save
            f.save(os.path.join(uploads_dir,f.filename))
            full_filename = os.path.join(
                app.config['UPLOAD_FOLDER'], "1.jpg")
            img=plt.imread(f.filename)

            if request.form.get('Style'):
                
                res = cv2.stylization(img, sigma_s=60, sigma_r=0.6)
                plt.imsave(f.filename+" Style.jpg",res)
            if request.form.get('Oil painting'):        
                res = cv2.xphoto.oilPainting(img,7,1)
                plt.imsave(f.filename+" Oil painting.jpg",res)
            if request.form.get('Pencil'):
                    
                dst_gray, dst_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
                plt.imsave(f.filename+" Pencil.jpg",dst_gray,cmap="gray")
            if  request.form.get('Cartoon'):
                originalmage=plt.imread(f.filename)
                colorImage = cv2.bilateralFilter(originalmage, 7, 75, 300)
                figure=plt.figure(figsize=(10,10))
                grayImage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2GRAY)
                getEdge = cv2.adaptiveThreshold(grayImage, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)            
                Image = cv2.medianBlur(originalmage, 9)
                res = cv2.bitwise_and(Image, Image, mask=getEdge)
                plt.imsave(f.filename+"Cartoon.jpg",res)
                
            
            return jsonify(filename=f.filename,
                           full_filename=full_filename
                           )
            # return render_template("success.html", name=f.filename, status="imagegrey_img",  user_image=full_filename)
        else:
            return jsonify(error="file not found")
    else:
        # return render_template("index.html")
        return jsonify(error="GET method not allowed")
if __name__=="__main__":
    app.run(port=5000,debug=True)