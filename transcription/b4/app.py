#rahul pandit
from flask import Flask, request, jsonify, json, make_response, redirect, session, send_from_directory,flash

from flask import Flask, render_template, flash, redirect, url_for, session, request, logging,make_response
import pandas as pd
import json

app = Flask(__name__)

@app.route('/',methods=['GET'])
def thanks():

	patients_df = pd.read_json('./static/k.json')
	
	#convert aws json data in javascript readable format

	AsyncData=[]

	for i in range(0,len(patients_df['results']['items'])):
	    #print(i,patients_df['results']['items'][i])
	    
	    firstItem=patients_df['results']['items'][i] #list item
	    if len(firstItem)==4:
	        firstItem['start_time']
	        firstItem['end_time']
	        firstItem['alternatives'][0]['content']
	        
	        {'end':firstItem['end_time'],'start':firstItem['start_time'],'text':firstItem['alternatives'][0]['content']}
	        
	        
	        AsyncData.append({'end':firstItem['end_time'],'start':firstItem['start_time'],'text':firstItem['alternatives'][0]['content']})


	ext='mp3'

	fileName="http://localhost:5000/static/sample.json"

	return render_template('transcript.html',AsyncData=AsyncData,fileFormat=True,fileName=fileName)



@app.route('/TranscriptSpeakerEditable',methods=['GET','POST'])
def TranscriptSpeakerEditable():
	old_data=request.form['old_value']
	new_data=request.form['new_value']

	print(old_data,new_data)

	send_data = {"data1":new_data,"data2":new_data,"sucess":True}
	return make_response(jsonify(send_data), 200)











if __name__ == '__main__':
	app.run(debug=True,host='localhost')