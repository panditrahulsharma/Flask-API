from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import pandas as pd
import json

app = Flask(__name__)

@app.route('/')
@app.route('/thanks')
def thanks():

	return render_template('subtitle.html')

if __name__ == '__main__':
	app.run(debug=True,host='localhost')

