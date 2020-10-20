from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask import Flask, request, jsonify, json, make_response, redirect, session, send_from_directory,flash

import random 

from time import sleep

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('dynamic.html')


@app.route('/ajax_get_data',methods=['GET','POST'])
def ajaxdata():
	send_data = [{"name":"00.01.23","length":"00.03.23","leng":"dqdqwd","status":'sucess'},{"name":"00.23.23","length":"00.13.23","leng":"en-gb","upload":"8-oct","status":'sucess'}];
	# send_data = [{"name":"00.01.23","length":"00.03.23","leng":"en-gb","upload":"7-oct","status":'sucess'}];

	return make_response(jsonify(send_data), 200)


@app.route('/ajax_post',methods=['GET','POST'])
def ajaxpost():
	print("request comming ...",request.form['new_value'])
	send_data = {"name":request.form['new_value'],"sucess":True}
	sleep(1)
	return make_response(jsonify(send_data), 200)




if __name__ == '__main__':
    app.run(debug=True)

    