#rahul pandit

from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import pandas as pd
import json
from FileFormat import is_video_file

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

	# print(AsyncData)

	#fileFormat=True it means it is a vedio file
	#else it is audio file

	ext='mp3'

	return render_template('transcript.html',AsyncData=AsyncData,fileFormat=is_video_file(ext))

if __name__ == '__main__':
	app.run(debug=True,host='localhost')