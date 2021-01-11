from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask import Flask, request, jsonify, json, make_response, redirect, session, send_from_directory,flash
import pandas as pd
import json


from BigData import SearchResult

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/searchTags',methods=['GET','POST'])
def searchTags():
	Tag=request.form['Tag']
	print(Tag)
	# lets search result
	obj = SearchResult(Tag)
	
	SearchData=obj.returnResult()
	ext=obj.returnExtensions()
	totalResult=obj.Totalresults()

	print(totalResult[1])
	return make_response(jsonify({"success":True,"SearchResult":SearchData,"ext":ext,"countByext":totalResult[1]}))

if __name__ == '__main__':
	app.run(debug=True)

