"""
1.first put upload folder in static folder
2.use statuc url in app(__main__,static_url)
3.app.config['']
4.url=localhost:4000/uploads/filename

"""


import time
from absl import app, logging
import cv2
import numpy as np
import tensorflow as tf
from yolov3_tf2.models import (YoloV3, YoloV3Tiny)
from yolov3_tf2.dataset import transform_images, load_tfrecord_dataset
from yolov3_tf2.utils import draw_outputs
from flask import Flask, request, Response, jsonify, send_from_directory, abort
import os
######################################################database################################
#rahul pandit

from flask import *
from flask import Flask, request, jsonify, json, make_response, redirect, session, send_from_directory
import MySQLdb
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import timedelta #for time to define how long session is active
import os
#import magic
import urllib.request
#from app import app
from werkzeug.utils import secure_filename
import cv2
#########################################################################################


# customize your API through the following parameters
classes_path = './data/labels/obj.names'
weights_path = './weights/yolov3.tf'
tiny = False                    # set to True if using a Yolov3 Tiny model
size = 416                      # size images are resized to for model
output_path = './static/detections/'   # path to output folder where images with detections are saved
num_classes = 1                # number of classes in model

# load in weights and classes
physical_devices = tf.config.experimental.list_physical_devices('GPU')
if len(physical_devices) > 0:
	tf.config.experimental.set_memory_growth(physical_devices[0], True)

if tiny:
	yolo = YoloV3Tiny(classes=num_classes)
else:
	yolo = YoloV3(classes=num_classes)

yolo.load_weights(weights_path).expect_partial()
print('weights loaded')

class_names = [c.strip() for c in open(classes_path).readlines()]
print('classes loaded')

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

#UPLOAD_FOLDER = '/home/rahul/Documents/yolo-api/static/upload/'

UPLOAD_FOLDER = '/home/rahul/Documents/yolo-api/static/uploads/'


# Initialize Flask application
app = Flask(__name__, static_url_path='')

app.permanent_session_lifetime = timedelta(days=5)

app.secret_key = "hello" #encrypt data by this key on server
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

conn = MySQLdb.connect(host="localhost",user="root",password="root@123",db="rahul")



@app.route('/')
def upload():
	return render_template('upload.html',user_info='Object Detection using Yolov3,Tensorflow')


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	

@app.route('/result')
def result():
	return render_template('result.html',user_info='Object Detection using Yolov3,Tensorflow')

@app.route('/file/<path:path>')
def send_js(path):
    return send_from_directory('uploads', path)


@app.route('/python-flask-files-upload', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	if 'files[]' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	
	files = request.files.getlist('files[]')
	errors = {}
	success = False
	
	#i am return image shape
	result=[]
	for file in files:
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			print(filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

			#file.save(os.path.join(os.getcwd(), filename))

			##############################################################yolo code#########################################
			file_path=app.config['UPLOAD_FOLDER']+filename
			print(file_path)
			img_raw = tf.image.decode_image(
				open(file_path, 'rb').read(), channels=3)
			img = tf.expand_dims(img_raw, 0)
			img = transform_images(img, size)
			t1 = time.time()
			boxes, scores, classes, nums = yolo(img)
			t2 = time.time()
			print('time: {}'.format(t2 - t1))

			print('detections:')
			for i in range(nums[0]):
				print('\t{}, {}, {}'.format(class_names[int(classes[0][i])],
												np.array(scores[0][i]),
												np.array(boxes[0][i])))
			img = cv2.cvtColor(img_raw.numpy(), cv2.COLOR_RGB2BGR)
			img = draw_outputs(img, (boxes, scores, classes, nums), class_names)
			#predicted_img_path=app.config['UPLOAD_FOLDER'] + 'detection1.jpg'
			#print(predicted_img_path)

			ext = filename.split(".")[-1]
			name = filename.split(".")[:-1]
			file_name = name[0] + '_' + '_final' + '.' + ext
			print(file_name)
			cv2.imwrite(app.config['UPLOAD_FOLDER']+file_name, img)

			#cv2.imwrite(predicted_img_path, img)
			#print('output saved to: {}'.format(predicted_img_path + 'detection1.jpg'))
			
			# prepare image for response
			_, img_encoded = cv2.imencode('.png', img)
			response = img_encoded.tostring()
			
			#remove temporary image
			#os.remove(filename)
			#success = True
			
			resp = {'message' :'result','success': True, 'image': 'http://127.0.0.1:4000/uploads/'+file_name}
			return make_response(jsonify(resp))
		else:
			errors[file.filename] = 'File type is not allowed'
	
	if success and errors:
		errors['message'] = 'File(s) successfully uploaded'
		resp = jsonify(errors)
		resp.status_code = 206
		return resp
	if success:     
		resp = jsonify({'message' :'ok'})
		resp.status_code = 201
		return resp
	else:
		resp = jsonify(errors)
		resp.status_code = 400
		return resp
"""
***************stop ******************
"""




@app.route('/image', methods= ['POST'])
def get_image():
	image = request.files["images"]
	image_name = image.filename
	image.save(os.path.join(os.getcwd(), image_name))

	img_raw = tf.image.decode_image(
		open(image_name, 'rb').read(), channels=3)
	img = tf.expand_dims(img_raw, 0)
	img = transform_images(img, size)
	t1 = time.time()
	boxes, scores, classes, nums = yolo(img)
	t2 = time.time()
	print('time: {}'.format(t2 - t1))

	print('detections:')
	for i in range(nums[0]):
		print('\t{}, {}, {}'.format(class_names[int(classes[0][i])],
										np.array(scores[0][i]),
										np.array(boxes[0][i])))
	img = cv2.cvtColor(img_raw.numpy(), cv2.COLOR_RGB2BGR)
	img = draw_outputs(img, (boxes, scores, classes, nums), class_names)
	cv2.imwrite(output_path + 'detection.jpg', img)
	print('output saved to: {}'.format(output_path + 'detection.jpg'))
	
	# prepare image for response
	_, img_encoded = cv2.imencode('.png', img)
	response = img_encoded.tostring()
	
	#remove temporary image
	os.remove(image_name)
	print("********************************************************************")
	print(response)
	print("*********************************************************************")
	try:
		return Response(response=response, status=200, mimetype='image/png')
	except FileNotFoundError:
		abort(404)



if __name__ == '__main__':
	app.run(debug=True, host = '0.0.0.0', port=4000)