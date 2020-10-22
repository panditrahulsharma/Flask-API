from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask import Flask, request, jsonify, json, make_response, redirect, session, send_from_directory,flash

import pandas as pd
import json
import random
import string

app = Flask(__name__)

@app.route('/')
@app.route('/thanks')
def thanks():
	return render_template('index.html')


@app.route('/live')
def live():
	return render_template('live.html')


def randomString(stringLength=10):
	"""Generate a random string of fixed length """
	letters = string.ascii_letters
	return ''.join(random.choice(letters) for i in range(stringLength))



@app.route('/today_employee',methods=['GET','POST'])
def todayemployee():
	send_data = [{"name":randomString(20),"email":randomString(20),'contact':randomString(20),"sucess":True},{"name":randomString(20),"email":randomString(20),'contact':randomString(20),"sucess":True},{"name":randomString(20),"email":randomString(20),'contact':randomString(20),"sucess":True}]
	return make_response(jsonify(send_data), 200)


@app.route('/employee_count',methods=['GET','POST'])
def employeecount():
	present=random.randint(1,100)
	Absent=100-present
	send_data = {"Present":present,"Absent":Absent,"sucess":True}
	return make_response(jsonify(send_data), 200)




@app.route('/ajax_get',methods=['GET','POST'])
def ajaxget():

	send_data = {"name":randomString(20),"email":randomString(20),'contact':randomString(20),"sucess":True}
	return make_response(jsonify(send_data), 200)



if __name__ == '__main__':
	app.run(debug=True,host='localhost')

