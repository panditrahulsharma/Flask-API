from flask import *
from flask import Flask, request, jsonify, json, make_response, redirect, session, send_from_directory
import MySQLdb
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)

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

				return redirect(url_for("home",data=user)) #data is a variable you can use any to send for home page
			else:
				return render_template("signup.html", title="Invalid details")	
			
		else:
			pass
	except Exception as e:
		return render_template("signup.html", title="Try again")





@app.route("/home")
def home():
	return render_template("home.html",user_data=request.args.get('data')) #don't mind user_data its random name you can use your own this is reflect on home page

if __name__ == "__main__":
	app.run(debug=True,port=4000)




