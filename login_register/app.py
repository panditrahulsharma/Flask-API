#rahul pandit

from flask import *
from flask import Flask, request, jsonify, json, make_response, redirect, session, send_from_directory
import MySQLdb
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import timedelta #for time to define how long session is active

#create session in flask 
#https://www.youtube.com/watch?v=iIhAfX4iek0
#https://techwithtim.net/tutorials/flask/sessions/

app = Flask(__name__)

app.permanent_session_lifetime = timedelta(days=5)

app.secret_key = "hello" #encrypt data by this key on server

conn = MySQLdb.connect(host="localhost",user="root",password="Root@123",db="rahul")

@app.route("/")
def index():
	return render_template("signup.html", title="Flask signUp form")

@app.route("/signUp", methods=['GET', 'POST'])
def signUp():
	try:
		if request.method=='POST':
			username = str(request.form["uname"])
			password = str(request.form["pswd"])
			email = str(request.form["email"])

			cursor = conn.cursor() #make a pointer
			cursor.execute("SELECT name FROM user WHERE email ='"+email+"'") #check user is exist or not
			user = cursor.fetchall()
			
			if len(user) >0: #if length is greater 1 then user email is exist
				return render_template("signup.html", title="User already Exist please try again another email")
			
			else:      #user not exist insert detail in database

				cursor.execute("INSERT INTO user (name,password,email)VALUES(%s,%s,%s)",(username,password,email))
				conn.commit()
				return redirect(url_for("login"))		
			
		else:
			pass
	except Exception as e:
		return render_template("signup.html", title=e)

	

@app.route("/login")
def login():
	return render_template("login.html",title="Flask Login Form")




@app.route("/checkUser",methods=["POST"])
def check():
	try:
		if request.method=='POST':
			email = str(request.form["email"])
			password = str(request.form["pswd"])

			cursor = conn.cursor()
			cursor.execute("SELECT * FROM user WHERE email ='"+email+"' and password='"+password+"' ")
			user = cursor.fetchall()
			
			if len(user) >0:
				for value in user:
					print(value)	
					#https://stackoverflow.com/questions/26954122/how-can-i-pass-arguments-into-redirecturl-for-of-flask
				session.permanent = True 
				session['email']=email #if i user is exist at login time then create session and redirect to profile

				return redirect(url_for("user")) #data is a variable you can use any to send for home page

			else:
				return render_template("login.html", title="Invalid details")	
			
		else:
			if "email" in session:  #when user try to go login page it automatically redirect to profile page
				return redirect(url_for("user"))

			return render_template("login.html")

	except Exception as e:
		return render_template("login.html", title="Try again") #any excepton and error occured redirect page into register






@app.route("/user")
def user():
	if "email" in session:
		email = session["email"]

		#now fetch all information of users
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM user WHERE email ='"+email+"' ")
		account = cursor.fetchall()
		print(account)
		return render_template("home.html",user_info=account[0])
	else:
		return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
	app.run(debug=True,port=4000)




