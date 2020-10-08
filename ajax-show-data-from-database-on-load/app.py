from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask import Flask, request, jsonify, json, make_response, redirect, session, send_from_directory,flash

import random 

from time import sleep

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')



@app.route('/ajax_get_data',methods=['GET','POST'])
def ajaxdata():

	send_data = [{"name":"What is RPA: Robotic Process Automation","length":"2m","leng":"en-gb","upload":"7-oct","status":'sucess'},{"name":"python","length":"4m","leng":"en-gb","upload":"8-oct","status":'sucess'}];
	return make_response(jsonify(send_data), 200)



@app.route('/uploaFile',methods=['GET','POST'])
def uploaFile():

	print("---------------------------------------------------- start ----------------------------------------------------------")

	language=request.form['language']
	print(language)
	file = request.files.getlist('files[]')[0]
	filename=file.filename
	random_id_lenght=request.form['random_id_lenght']
	random_id_status=request.form['random_id_status']
	# ///////////////////////////////////////////////////////////////////////////////////////////////////
	r1 = random.randint(5, 15) 
	print("sleep time=",r1)

	# sleep(r1)
	send_data = [{"name":filename,"length":(str(r1)+"m"),"leng":language,"upload":"7-oct","status":'sucess',"random_id_lenght":random_id_lenght,"random_id_status":random_id_status}];
	return make_response(jsonify(send_data), 200)
	print("---------------------------------------------------- end ----------------------------------------------------------")



@app.route('/DashboardData',methods=['GET', 'POST'])  
@app.route('/DashboardData/<WorkSpace>',methods=['GET', 'POST'])    
@app.route('/DashboardData/<WorkSpace>/<NewFolder>',methods=['GET', 'POST'])
def DashboardData(WorkSpace=None, NewFolder=None):
	if not WorkSpace and not NewFolder:
		send_data = [{"name":"python","length":"4m","leng":"en-gb","upload":"8-oct","status":'sucess'}];
		return make_response(jsonify(send_data), 200)
	elif WorkSpace and not NewFolder:
		send_data = [{"name":"What is RPA: Robotic Process Automation","length":"2m","leng":"en-gb","upload":"7-oct","status":'sucess'},{"name":"python","length":"4m","leng":"en-gb","upload":"8-oct","status":'sucess'}];
		return make_response(jsonify(send_data), 200)
	elif WorkSpace and NewFolder:
		send_data = [{"name":"What is RPA: Robotic Process Automation","length":"2m","leng":"en-gb","upload":"7-oct","status":'sucess'},{"name":"What is RPA: Robotic Process Automation","length":"2m","leng":"en-gb","upload":"7-oct","status":'sucess'},{"name":"python","length":"4m","leng":"en-gb","upload":"8-oct","status":'sucess'}];
		return make_response(jsonify(send_data), 200)
	else:
		return "not match"



@app.route('/Dashboard',methods=['GET', 'POST'])  
@app.route('/Dashboard/<WorkSpace>',methods=['GET', 'POST'])    
@app.route('/Dashboard/<WorkSpace>/<NewFolder>',methods=['GET', 'POST'])
def Dashboard(WorkSpace=None, NewFolder=None):
	if not WorkSpace and not NewFolder:
		send_data = [{"name":"What is RPA: Robotic Process Automation","length":"2m","leng":"en-gb","upload":"7-oct","status":'sucess'},{"name":"python","length":"4m","leng":"en-gb","upload":"8-oct","status":'sucess'}];
		# return make_response(jsonify(send_data), 200)
		return render_template("dashboard.html")
	elif WorkSpace and not NewFolder:
		return render_template("dashboard.html")
	elif WorkSpace and NewFolder:
		return render_template("dashboard.html")
	else:
		return "not match"


if __name__ == '__main__':
    app.run(debug=True)

    