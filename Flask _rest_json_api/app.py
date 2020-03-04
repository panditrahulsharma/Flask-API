#rahul pandit

from flask import *
from flask import Flask, request, jsonify, json, make_response, redirect, session, send_from_directory
import MySQLdb
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import timedelta #for time to define how long session is active

#**********************************************************

import base64 #add new
#generate random string
import string 
import random 

#****************************************************************88


app = Flask(__name__)

app.permanent_session_lifetime = timedelta(days=5)

app.secret_key = "hello" #encrypt data by this key on server

conn = MySQLdb.connect(host="localhost",user="root",password="root@123",db="rahul")






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


#download and save image
def convert_base(base64_img,name,ext):
	base64_img_bytes = base64_img.encode('utf-8')
	with open(name+ext, 'wb') as file_to_save:
	    decoded_image_data = base64.decodebytes(base64_img_bytes)
	    file_to_save.write(decoded_image_data)
	print("******************successfull download image ********************")




@app.route("/processjson",methods=['POST','GET'])
def processjson():
	#accept json data
	data=request.get_json()
	vehicle_name=data['vehicle_name']
	Brand=data['brand']
	model=data['model']
	img1_str=data['img1']

	#call function random_str() to generate random string
	random_name=random_str()
	#convert_base function pass image base64_string,name,ext
	convert_base(img1_str,random_name[0],'.jpeg') #convert base64_string to img

	return jsonify({'result':'successfull Get','vehicle_name':vehicle_name,'Brand':Brand,'model':model,'img1':img1_str})



if __name__ == "__main__":
	app.run(debug=True,port=4000)




