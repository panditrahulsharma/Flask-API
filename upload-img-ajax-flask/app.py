#rahul pandit

from flask import *
from flask import Flask, request, jsonify, json, make_response, redirect, session, send_from_directory
import MySQLdb
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import timedelta #for time to define how long session is active
import os
#import magic
import urllib.request
#from app import app
from werkzeug.utils import secure_filename

#create session in flask 
#https://www.youtube.com/watch?v=iIhAfX4iek0
#https://techwithtim.net/tutorials/flask/sessions/

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

UPLOAD_FOLDER = '/home/rahul/Music/flask-api/demo/upload'


app = Flask(__name__)

app.permanent_session_lifetime = timedelta(days=5)

app.secret_key = "hello" #encrypt data by this key on server
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024




conn = MySQLdb.connect(host="localhost",user="root",password="root@123",db="rahul")

@app.route("/")
def index():
	if "email" in session:
		return redirect(url_for("upload"))
	else:		
		return render_template("signup.html", title="Flask signUp form")

@app.route("/signUp", methods=['GET', 'POST'])
def signUp():
	try:
		if request.method=='POST':
			username = str(request.form["uname"])
			password = str(request.form["pswd"])
			email = str(request.form["email"])

			cursor = conn.cursor() #make a pointer
			cursor.execute("SELECT name FROM users WHERE email ='"+email+"'") #check user is exist or not
			user = cursor.fetchall()
			
			if len(user) >0: #if length is greater 1 then user email is exist
				return render_template("signup.html", title="User already Exist please try again another email")
			
			else:      #user not exist insert detail in database

				cursor.execute("INSERT INTO users (name,password,email)VALUES(%s,%s,%s)",(username,password,email))
				conn.commit()
				session.permanent = True 
				session['email']=email #if i user is exist at login time then create session and redirect to profile
				return redirect(url_for("upload"))		
			
		else:
			pass
	except Exception as e:
		return render_template("signup.html", title=e)

	

@app.route("/login")
def login():
	if "email" in session:
		return redirect(url_for("upload"))
	else:

		return render_template("login.html",title="Flask Login Form")




@app.route("/checkUser",methods=["POST"])
def check():
	try:
		if request.method=='POST':
			email = str(request.form["email"])
			password = str(request.form["pswd"])

			cursor = conn.cursor()
			cursor.execute("SELECT * FROM users WHERE email ='"+email+"' and password='"+password+"' ")
			user = cursor.fetchall()
			
			if len(user) >0:
					#https://stackoverflow.com/questions/26954122/how-can-i-pass-arguments-into-redirecturl-for-of-flask
				session.permanent = True 
				session['email']=email #if i user is exist at login time then create session and redirect to profile

				return redirect(url_for("upload")) #data is a variable you can use any to send for home page

			else:
				return render_template("login.html", title="Invalid details")	
			
		else:
			if "email" in session:  #when user try to go login page it automatically redirect to profile page
				return redirect(url_for("upload"))

			return render_template("login.html")

	except Exception as e:
		return render_template("login.html", title="Try again") #any excepton and error occured redirect page into register






@app.route("/user")
def user():
	if "email" in session:
		email = session["email"]

		#now fetch all information of users
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM users WHERE email ='"+email+"' ")
		account = cursor.fetchall()
		print(account)
		return render_template("profile.html",user_info=account[0])
	else:
		return redirect(url_for("login"))

"""
***************upload file code here start******************
"""

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/upload')
def upload():
	if "email" in session:
		email=session["email"]
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM users WHERE email ='"+email+"' ")
		account = cursor.fetchall()
		return render_template('upload.html',user_info=account[0])
	else:
		return redirect(url_for("login"))

@app.route('/python-flask-files-upload', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	if 'files[]' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	
	files = request.files.getlist('files[]')
	
	print(files)

	errors = {}
	success = False
	
	for file in files:
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			success = True
		else:
			errors[file.filename] = 'File type is not allowed'
	
	if success and errors:
		errors['message'] = 'File(s) successfully uploaded'
		resp = jsonify(errors)
		resp.status_code = 206
		return resp
	if success:
		resp = jsonify({'message' : '***************Result ******************'})
		resp.status_code = 201
		return resp
	else:
		resp = jsonify(errors)
		resp.status_code = 400
		return resp
"""
***************stop ******************
"""



@app.route("/logout")
def logout():
    session.pop("email", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
	app.run(debug=True,port=4000)




