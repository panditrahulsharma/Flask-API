#rahul pandit

from flask import *
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask import Flask, request, jsonify, json, make_response, redirect, session, send_from_directory
import MySQLdb
from flask_mysqldb import MySQL
import random
import string
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from datetime import timedelta #for time to define how long session is active
import threading
from SendconfimationEmail import sendConfirmation
from werkzeug.utils import secure_filename
import os
#====================================
# settings.py
from dotenv import load_dotenv
load_dotenv()
# ===================================


#create session in flask 
#https://www.youtube.com/watch?v=iIhAfX4iek0
#https://techwithtim.net/tutorials/flask/sessions/

app = Flask(__name__)


app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = "./static/PaperFolder/"
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024

# app.permanent_session_lifetime = timedelta(days=5)
app.secret_key = "hello" #encrypt data by this key on server
conn = MySQLdb.connect(host="localhost",user="root",password="Meta@123",db="SubmitPaper")

ALLOWED_EXTENSIONS = set(['.docx', 'pdf'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	

def randomString(stringLength=10):
	"""Generate a random string of fixed length """
	letters = string.ascii_letters
	return ''.join(random.choice(letters) for i in range(stringLength))



@app.route("/", methods=['GET','POST'])
def index():
	return render_template("submit-form.html")


@app.route("/testing", methods=['GET','POST'])
def testing():
	return make_response(jsonify({"success":True}),200)


@app.route("/Submitpaper", methods=['GET','POST'])
def Submitpaper():
	#add try catch here
	try: 
		cursor = conn.cursor() #make a pointer
		if 'files[]' not in request.files:
			resp = jsonify({'message' : 'No file part in the request',"success":False})
			resp.status_code = 400
			return resp
		
		files = request.files.getlist('files[]')
		
		errors = {}
		success = False
		
		for file in files:
			print(file)
			if file and allowed_file(file.filename):
				filename = secure_filename(file.filename)
				uid = ''.join(random.choice(string.ascii_letters) for _ in range(26))

				ext = filename.split(".")[-1]
				filename = uid+'.'+ext

				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
				success = True

				# data for contact
				Volume=request.form['Volume']
				PaperName=request.form['PaperName']
				FirstName=request.form['FirstName']
				LastName=request.form['LastName']
				Country=request.form['Country']
				Organization=request.form['Organization']
				Email=request.form['Email']

				cursor.execute("INSERT INTO GeneralInformation (Volume,PaperName,FirstName,LastName,Country,Organization,Email)VALUES(%s,%s,%s,%s,%s,%s,%s)",(Volume,PaperName,FirstName,LastName,Country,Organization,Email));
				General_Id=cursor.lastrowid

				# insert data into general info
				Author=request.form['Author']
				AuthorEmail=request.form['AuthorEmail'],
				Telephone=request.form['Telephone'],
				KeyWords=request.form['KeyWords'],
				FilePath=filename
				
				
				ProjectId=randomString()
				cursor.execute("INSERT INTO ContactAuthorDetails (General_Id,Author,AuthorEmail,Telephone,KeyWords,FilePath,PraperId,status,created_at)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(General_Id,Author,AuthorEmail,Telephone,KeyWords,FilePath,ProjectId,False,datetime.datetime.now()));
				Contact_Id=cursor.lastrowid

				user_data={"ProjectId":ProjectId,"PaperName":PaperName,"AuthorEmail":AuthorEmail}
				t1 = threading.Thread(target=sendConfirmation,args=(user_data,))
				print("start sending mail.....")
				t1.start()
				conn.commit()
				return make_response(jsonify({"General_Id": General_Id,"Contact_Id":Contact_Id,"ProjectId":ProjectId,"success":True,"message":"file Upload success"}),200)
				t1.join()

			else:
				return make_response(jsonify({"success":False,"message":"file Extension not Valid .."}),200)

	except Exception as e:
		print(e)
		return make_response(jsonify({"success":False,"message":"Something Went Wrong.."}),200)




if __name__ == "__main__":
	app.run(debug=True,host='localhost')

