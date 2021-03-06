#rahul pandit
from flask import *
from flask import Flask, request, jsonify, json, make_response, redirect, session, send_from_directory
from flask_mysqldb import MySQL
import datetime
from flask_cors import CORS
from flask_mail import Mail,Message

from werkzeug.security import generate_password_hash, check_password_hash

import threading
import asyncio
import secrets
import os, string, random
from fastai import *
from fastai.vision import *
from fastai.callbacks.hooks import *
import os
import numpy as np
import cv2
import imutils
import subprocess



#**********************************************************
import base64 #add new
#generate random string
import string 
import random 
import base64
from io import BytesIO
from PIL import Image

#****************************************************************88


UPLOAD_FOLDER = '/home/rahul/Music/Developement/base64/uploads/'
MODEL_FOLDER = '/home/rahul/Music/Developement/model/'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)
CORS(app)

app.debug = True
app.env = 'development'
# app.config['SESSION_TYPE'] = 'filesystem'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root@123'
app.config['MYSQL_DB'] = 'development'
app.config['MAIL_SERVER'] = 'smtp.gmail.com' #'server229.web-hosting.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'funto236@gmail.com'#'support@metaorigins.com'
app.config['MAIL_DEFAULT_SENDER'] = 'funto@gmail.com'#'support@metaorigins.com'
app.config['MAIL_PASSWORD'] = 'funto@123'#'UwuW[X0zSP^@'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mysql = MySQL(app)
mail = Mail(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MODEL_FOLDER'] = MODEL_FOLDER


@app.route("/")
def index():
	return "successfull"

# initializing size of string 
def random_str():
    # initializing size of string 
    N = 100
    res1 = ''.join(random.choices(string.ascii_uppercase +string.digits, k = N)) 
    res2 = ''.join(random.choices(string.ascii_uppercase +string.digits, k = N)) 
    res3 = ''.join(random.choices(string.ascii_uppercase +string.digits, k = N)) 
    res4 = ''.join(random.choices(string.ascii_uppercase +string.digits, k = N)) 
    res5 = ''.join(random.choices(string.ascii_uppercase +string.digits, k = N)) 
    
    return [res1,res2,res3,res4,res5]


def convert_base_to_img(base64_img,name):
	image_data = bytes(base64_img, encoding="ascii")
	im = Image.open(BytesIO(base64.b64decode(image_data)))
	im.save(app.config['UPLOAD_FOLDER']+name+'.jpg')

	print("successfull uploads")

#base string
#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'



@app.route("/mobile_damage_check",methods=['POST','GET'])
def mobile_damage_check():

	#access form data
	img=[] #list
	vehicle_name = request.form['vehicle_name']
	Brand = request.form['Brand']
	Model = request.form['Model']
	img.append(request.form['img1'])
	img.append(request.form['img2'])
	img.append(request.form['img3'])
	img.append(request.form['img4'])
	img.append(request.form['img5'])
	
	print(vehicle_name)
	print(Brand)
	print(Model)
	print(type(vehicle_name))
	print(type(img[1]))
	#convert base64 imag1,img2,img3,img4,img5 to img and return file name to 
	
	#call function random_str() to generate random string
	random_name=random_str()	
	print(random_name)

	for i in range(0,len(random_name)):
		convert_base_to_img(img[i],random_name[i])

	return jsonify({'result':'successfull POST','vehicle_name':vehicle_name,'Brand':Brand,'Model':Model,'img1':random_name[0],'img2':random_name[1],'img3':random_name[2],'img4':random_name[3],'img5':random_name[4]})




@app.route("/processjson",methods=['POST','GET'])
def processjson():
	#accept json data
	data=request.get_json() #get dictonary using get_json() method from postman
	vehicle_name=data['vehicle_name']
	Brand=data['brand']
	model=data['model']
	img1_str=data['img1']

	#print(data)
	#call function random_str() to generate random string
	random_name=random_str()
	#convert_base function pass image base64_string,name,ext
	convert_base(img1_str,random_name[0]) #convert base64_string to img

	return jsonify({'result':'successfull Get','vehicle_name':vehicle_name,'Brand':Brand,'model':model,'img1':img1_str})



if __name__ == "__main__":
	app.run(debug=True,port=4000)




