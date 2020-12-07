from flask import Flask, render_template, url_for, request, abort
import os
import time
from datetime import timedelta #for time to define how long session is active
import secrets
from flask import Flask, request, jsonify, json, make_response, redirect, session, send_from_directory,flash
from time import sleep
import threading



app = Flask(__name__)

def DeleteExportFile(filename):
	sleep(10)
	os.remove('./static/'+filename)

@app.route('/')
def index():
	return render_template('index.html')


# use multithreading here
@app.route('/DeleteFiles',methods=['GET','POST'])
@app.route('/DeleteFiles/<UrlId>/<ServiceType>',methods=['GET','POST'])
def DeleteFiles(UrlId=None,ServiceType=None):
	# sleep(4)

	data=request.form['url']
	send_data = {'success': True,"file":data,'filename':"FileNameWithExt"}
	return make_response(jsonify(send_data), 200)



if __name__ == '__main__':
	app.run(debug=True,host='localhost',port='5000')
