from flask import Flask, render_template, url_for, request, abort
import os
import time
from datetime import timedelta #for time to define how long session is active
import secrets


app = Flask(__name__)


@app.route('/')
def subtitle():
	return render_template('subtitle.html')


if __name__ == '__main__':
	app.run(debug=True,host='localhost',port='8000')
