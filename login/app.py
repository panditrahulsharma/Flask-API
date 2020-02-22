from flask import Flask,render_template,request,redirect,url_for
import MySQLdb

app = Flask(__name__)

conn = MySQLdb.connect(host="localhost",user="root",password="Root@123",db="rahul")

@app.route("/")
def index():
	return render_template("signup.html", title="SignUP")

@app.route("/signUp", methods=['GET', 'POST'])
def signUp():
	username = str(request.form["uname"])
	password = str(request.form["pswd"])
	email = str(request.form["email"])
	
	cursor = conn.cursor()
	
	cursor.execute("INSERT INTO user (name,password,email)VALUES(%s,%s,%s)",(username,password,email))
	conn.commit()
	return redirect(url_for("login"))
	

@app.route("/login")
def login():
	return render_template("login.html",title="data")




@app.route("/checkUser",methods=["POST"])
def check():
	email = str(request.form["email"])
	password = str(request.form["pswd"])
	cursor = conn.cursor()
	cursor.execute("SELECT name FROM user WHERE email ='"+email+"'")
	user = cursor.fetchall()
	
	if len(user) >0:
		for value in user:
		    print(value)		
		return redirect(url_for("home"))
	else:
		return "failed"



@app.route("/home")
def home():
	return render_template("home.html")

if __name__ == "__main__":
	app.run(debug=True,port=4000)




