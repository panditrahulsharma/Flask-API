from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask import Flask, request, jsonify, json, make_response, redirect, session, send_from_directory,flash

import pandas as pd
import json

from pyutil import filereplace



app = Flask(__name__)

@app.route('/')
@app.route('/thanks')
def thanks():
	return render_template('subtitle.html')


@app.route('/ajax_post',methods=['GET','POST'])
def ajaxpost():
	print("request comming ...",request.form['new_value'])

	old_data=request.form['old_value']
	new_data=request.form['new_value']

	print("old_data=",old_data)
	print("new_data=",new_data)

	fileName = './static/rpa.srt'
	# Read in the file
	with open(fileName) as r:
	  text = r.read().replace(old_data,new_data)
	with open(fileName, "w") as w:
	  w.write(text)


	send_data = {"data1":new_data,"data2":new_data,"sucess":True}
	return make_response(jsonify(send_data), 200)





if __name__ == '__main__':
	app.run(debug=True,host='localhost')

