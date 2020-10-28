#rahul pandit
from flask import Flask, request, jsonify, json, make_response, redirect, session, send_from_directory,flash

from flask import Flask, render_template, flash, redirect, url_for, session, request, logging,make_response
import pandas as pd
import json

app = Flask(__name__)

@app.route('/',methods=['GET'])
def thanks():

	# patients_df = pd.read_json('./static/sample.json')
	

	joe_aws = open("./static/sample.json")
	joe_aws = json.load(joe_aws)


	#convert aws json data in javascript readable format

	# AsyncData=[]

	# for i in range(0,len(patients_df['results']['items'])):
	#     #print(i,patients_df['results']['items'][i])
	    
	#     firstItem=patients_df['results']['items'][i] #list item
	#     if len(firstItem)==4:
	#         firstItem['start_time']
	#         firstItem['end_time']
	#         firstItem['alternatives'][0]['content']
	        
	#         {'end':firstItem['end_time'],'start':firstItem['start_time'],'text':firstItem['alternatives'][0]['content']}
	        
	        
	#         AsyncData.append({'end':firstItem['end_time'],'start':firstItem['start_time'],'text':firstItem['alternatives'][0]['content']})

	AsyncData=[]

	for i in range(0,len(joe_aws)):
	    for j in range(0,len(joe_aws[i]['words'])):
	        AsyncData.append({'end':joe_aws[i]['words'][j]['end_time'],'start':joe_aws[i]['words'][j]['start_time'],'text':joe_aws[i]['words'][j]['text']})
	    

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