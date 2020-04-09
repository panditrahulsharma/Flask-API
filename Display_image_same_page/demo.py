from flask import *
from flask import Flask, request, jsonify, json, make_response, redirect, session, send_from_directory
from flask_mysqldb import MySQL
import datetime
from flask_cors import CORS
from flask_mail import Mail,Message

from werkzeug.security import generate_password_hash, check_password_hash

import threading
import asyncio
import secrets
import os, string, random
from fastai import *
from fastai.vision import *
from fastai.callbacks.hooks import *
import os
import numpy as np
import cv2
import imutils
import subprocess

#**********************************************************
import base64 #add new
#generate random string
import string 
import random 
import base64
from io import BytesIO
from PIL import Image
from base64 import b64decode
import os.path
import cv2

from time import sleep
#****************************************************************88


UPLOAD_FOLDER = '/home/rahul/Music/Developement/uploads/'
MODEL_FOLDER = '/home/rahul/Music/Developement/model/'


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__, static_url_path='')
app.secret_key = secrets.token_urlsafe(16)
CORS(app)

app.debug = True
app.env = 'development'
# app.config['SESSION_TYPE'] = 'filesystem'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root@123'
app.config['MYSQL_DB'] = 'development'
app.config['MAIL_SERVER'] = 'smtp.gmail.com' #'server229.web-hosting.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'funto236@gmail.com'#'support@metaorigins.com'
app.config['MAIL_DEFAULT_SENDER'] = 'funto@gmail.com'#'support@metaorigins.com'
app.config['MAIL_PASSWORD'] = 'funto@123'#'UwuW[X0zSP^@'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mysql = MySQL(app)
mail = Mail(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MODEL_FOLDER'] = MODEL_FOLDER

@app.route('/')
def hello_world():
    return 'Hello World!'



################################  7-apr-2020 #############################

@app.route("/r")
def inseption(): 
    return render_template("upload2.html", title="Flask signUp form")



@app.route('/upload_multiple', methods=['POST'])
def upload_multiple():
    try:
        if request.method == 'POST':
            files = request.files.getlist('files[]')
            for file in files:
                if file and allowed_file(file.filename):
                    uid = randomString(10)
                    filename = file.filename
                    ext = filename.split(".")[-1]
                    name = filename.split(".")[:-1]
                    file_name = name[0]+'_'+uid+'.'+ext
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
            #flash('File(s) successfully uploaded')
            return make_response(jsonify(send_data), 200)

    except Exception as e:
        print(str(e))
"""        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        send_data = {'success': False}
        return make_response(jsonify(send_data), 200)
"""

############################################################################






##################################mobile code################################


#*********************************mobile api*****************************************************
#*********************************mobile api*****************************************************
#*********************************mobile api*****************************************************
#*********************************mobile api*****************************************************
#*********************************mobile api*****************************************************
#*********************************mobile api*****************************************************



@app.route('/file/<path:path>')
def send_js(path):
    return send_from_directory('uploads', path)


@app.route("/mobile/register")
def mobile_registers(): 
    return render_template("register.html", title="Flask signUp form")


@app.route("/mobile/login")
def login_page():
    if "email" in session:
        return redirect(url_for("user"))
    else:       
        return render_template("login.html", title="Flask signUp form")



# initializing size of string 
def random_str():
    # initializing size of string 
    N = 100
    res1 = ''.join(random.choices(string.ascii_uppercase +string.digits, k = N)) 
    res2 = ''.join(random.choices(string.ascii_uppercase +string.digits, k = N)) 
    res3 = ''.join(random.choices(string.ascii_uppercase +string.digits, k = N)) 
    res4 = ''.join(random.choices(string.ascii_uppercase +string.digits, k = N)) 
    res5 = ''.join(random.choices(string.ascii_uppercase +string.digits, k = N)) 
    return [res1,res2,res3,res4,res5]

def convert_base_to_img(base64_img,name):
    image_data = bytes(base64_img, encoding="ascii")
    im = Image.open(BytesIO(base64.b64decode(image_data)))
    im.save(app.config['UPLOAD_FOLDER']+name+'.jpg')
    print("successfull uploads")

def convert_base_to_vedio(base64_vedio,name):
    bytes = b64decode(base64_vedio, validate=True)
    f = open(name+'.mp4', 'wb')
    f.write(bytes)
    f.close()






# http://localhost:5000/pythinlogin/register - this will be the registration page, we need to use both GET and POST requests
@app.route('/mobile_register', methods=['GET', 'POST'])
def mobile_register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'first_name' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        first_name = request.form['first_name']
        last_name ='sharma' #request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        company = '1'#request.form['company']
        location = '1'#request.form['location']
        password = generate_password_hash(request.form['password'])
        
                # Check if account exists using MySQL
        cursor = mysql.connection.cursor()
        #cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email ='"+email+"'")
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            return '{data:Account already exists!}'
            #msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            return '{data:Invalid email address!}'
            #msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', first_name):
            return '{data:Username must contain only characters and numbers!}'
            #msg = 'Username must contain only characters and numbers!'
        elif not first_name or not password or not email:
            return '{data:Please fill out the form!}'
            #msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute("INSERT INTO users (first_name, last_name,password, email, phone, company, location,created_at)"
                        "VALUES (%s, %s ,%s, %s,%s, %s ,%s, %s)",
                        (first_name, last_name, password, email, phone, company, location, datetime.datetime.now()))
            mysql.connection.commit()
            return jsonify({'data':'Register-success','first_name':first_name,'email':email,'password':password,'phone':phone})
            

    elif request.method == 'POST':
        # Form is empty... (no POST data)
        return '{data:Please fill out the form!}'
        #msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return '{data:Register faild}'
###############################
#login
##################
@app.route('/mobile_login', methods=['GET', 'POST'])
def mobile_login():
    # Output message if something goes wrong...
    msg = ' Output message if something goes wrong...'
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        # Create variables for easy access
        email = request.form['email']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor()

        cursor.execute("SELECT * FROM users WHERE email ='"+email+"'")
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account and check_password_hash(account[4], password):
            # Create session data, we can access this data in other routes
            #session['loggedin'] = True
            #session['id'] = account['id']
            #session['email'] = account['email']
            # Redirect to home page
            return jsonify({'data':'Login-success','email':email,'password':password})
        else:
            # Account doesnt exist or username/password incorrect
            #msg = 'Incorrect username/password!'
            return jsonify({'data':'Incorrect Email/password!'})
    # Show the login form with message (if any)
    #return render_template('index.html', msg=msg)
    return '{data:something goes wrong...}'



@app.route("/demo",methods=['POST','GET'])
def demo():
    email=request.form['email']
    print(len(email))
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO mobile_images (email,original_img1,original_img2,original_img3,original_img4,original_img5,original_vedio,process_img1,process_img2,process_img3,process_img4,process_img5,process_vedio,created_at)"
                "VALUES (%s, %s ,%s, %s,%s, %s ,%s,%s,%s,%s,%s,%s,%s,%s)",
                ('rahul@gmail.com','img1', 'img2','img3','img4','img5','original_vedio','process_img1','process_img2','process_img3','process_img4','process_img5','process_vedio',datetime.datetime.now()))
    mysql.connection.commit()
    cur.close()
    return jsonify({'data':email})
#**********************************************Register Mobile API*****************************************************************************
#**********************************************register Mobile ApI*****************************************************************************

@app.route("/mobile_damage_check",methods=['POST','GET'])
def mobile_damage_check():
    try:
        if request.method == 'POST':
            email = request.form['email']
            if not email:
                return jsonfy({'data':'Please first signin/signup'})
            #access form data
            img=[] #list
            random_name=random_str()    
            print(random_name)

            predict_img_names=[]

            email=request.form['email']
            vehicle_name = request.form['vehicle_name']
            Brand = request.form['Brand']
            Model = request.form['Model']
            img.append(request.form['img1'])
            img.append(request.form['img2'])
            img.append(request.form['img3'])
            img.append(request.form['img4'])
            img.append(request.form['img5'])
            
            #call function random_str() to generate random string


            for i in range(0,len(random_name)):
                #check base64 string then pass it to function
                if len(img[i])>0:
                    convert_base_to_img(img[i],random_name[i]) #convert base 64 to img ,pass img[i] it is base string and random[i] names that image store 

            

            #now load image one by one using open_image fastai function
            for i in range(0,len(random_name)):
                if len(img[i])>0: #check if string is exist then pass it to model
                    learn = setup_learner()
                    file_name=app.config['UPLOAD_FOLDER']+random_name[i]+'.jpg'

                    image = open_image(file_name)
                    # img = cv2.imread(file_name)
                    out_put = infer_imagewithcontours(image, learn) #pass img to function that create bounding box

                    out_put = cv2.cvtColor(out_put*255, cv2.COLOR_BGR2RGB) 

                    filename=random_name[i]+'_'+email+'_'+'.jpg' #save new files
                    
                    cv2.imwrite(app.config['UPLOAD_FOLDER']+filename, out_put) #saving image in a folder

                    predict_img_names.append(filename)  #appned name in predict_img_names list for sending return in json
                else:
                	predict_img_names.append('No image inserted')

            cur = mysql.connection.cursor()


            cur.execute("INSERT INTO mobile_images (email,original_img1,original_img2,original_img3,original_img4,original_img5,original_vedio,process_img1,process_img2,process_img3,process_img4,process_img5,process_vedio,created_at) VALUES (%s, %s ,%s, %s,%s, %s ,%s,%s,%s,%s,%s,%s,%s,%s)",(email,random_name[0],random_name[1],random_name[2],random_name[3],random_name[4],'original_vedio',predict_img_names[0],predict_img_names[1],predict_img_names[2],predict_img_names[3],predict_img_names[4],'process_vedio',datetime.datetime.now()))
            mysql.connection.commit()
            cur.close()

            return jsonify({'email':email,'random_name1':random_name[0],'random_name2':random_name[1],'random_name3':random_name[2],'random_name4':random_name[3],'random_name5':random_name[4],'predict_img_names1':predict_img_names[0],'predict_img_names2':predict_img_names[1],'predict_img_names3':predict_img_names[2],'predict_img_names4':predict_img_names[3],'predict_img_names5':predict_img_names[4]})
            #return jsonify({'result':'successfull POST','email':email,'vehicle_name':vehicle_name,'Brand':Brand,'Model':Model,'img1':random_name[0],'img2':random_name[1],'img3':random_name[2],'img4':random_name[3],'img5':random_name[4],'predict_img_names':predict_img_names,'length':x})

    except Exception as e:
        print(str(e))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        send_data = {'success': False}
        return make_response(jsonify(send_data), 200)


@app.route('/damage_check1', methods=['POST'])
def damage_check1():
    try:
        if request.method == 'POST':
            user_id = request.form['user_id']
            if not user_id:
                user_id = 1

            file = request.files['fileUpload']
            if file and allowed_file(file.filename):
                uid = randomString(10)
                filename = file.filename
                ext = filename.split(".")[-1]
                name = filename.split(".")[:-1]
                file_name = name[0]+'_'+uid+'.'+ext
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
                orig_img = file_name
                learn = setup_learner()
                img = open_image(app.config['UPLOAD_FOLDER']+'/'+file_name)
                out_put = infer_imagewithcontours(img, learn)
                # print(out_put)
                ext = filename.split(".")[-1]
                name = filename.split(".")[:-1]
                file_name = name[0] + '_'+uid+'_' + '_final' + '.' + ext

                out_put = cv2.cvtColor(out_put*255, cv2.COLOR_BGR2RGB)
                cv2.imwrite(app.config['UPLOAD_FOLDER']+'/'+file_name, out_put)
                process_img = file_name

                cur = mysql.connection.cursor()
                cur.execute(
                    "INSERT INTO images (user_id,original_img, process_img,created_at) "
                    "VALUES (%s, %s ,%s, %s)",
                    (user_id, orig_img, process_img, datetime.datetime.now()))
                mysql.connection.commit()
                cur.close()

            send_data = {'success': True, 'image': 'http://localhost:4000/file/'+file_name}
            return make_response(jsonify(send_data), 200)
    except Exception as e:
        print(str(e))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        send_data = {'success': False}
        return make_response(jsonify(send_data), 200)




#####################################END mobile Code#############################################


#**********************************************END mobile API*****************************************************************************
#**********************************************END mobile API*****************************************************************************
#**********************************************END mobile API*****************************************************************************
#**********************************************END mobile API*****************************************************************************
#**********************************************END mobile API*****************************************************************************




@app.route('/login', methods=['GET','POST'])
def login():
    try:
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            cur = mysql.connection.cursor()
            query = "SELECT password,first_name,last_name,id FROM users WHERE email ='"+email+"'"
            cur.execute(query)
            data = cur.fetchall()
            # print(data)
            if len(data) and check_password_hash(data[0][0], password):
                session['user_id'] = data[0][3]
                send_data = {'success': True, 'first_name': data[0][1], 'last_name': data[0][2], 'id': data[0][3]}
                print(session)
                return make_response(jsonify(send_data), 200)
            else:
                send_data = {'success': False}
                return make_response(jsonify(send_data), 200)
    except Exception as e:
        print(str(e))
        send_data = {'success': False}
        return make_response(jsonify(send_data), 200)


@app.route('/register', methods=['POST'])
def register():
    try:
        if request.method == 'POST':
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            phone = request.form['phone']
            company = request.form['company']
            location = request.form['location']
            password = generate_password_hash('Meta@123')
            

            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users (first_name, last_name,password, email, phone, company, location,created_at) "
                        "VALUES (%s, %s ,%s, %s,%s, %s ,%s, %s)",
                        (first_name, last_name, password, email, phone, company, location, datetime.datetime.now()))
            mysql.connection.commit()
            cur.close()
            # msg = Message('Welcome', recipients=[email])
            # thread1 = threading.Thread(target=mail.send(msg))
            # thread1.start()
            message = "hi,"+first_name+"<br>you have successfully created account on Metaorigin Labs.your username "+email+", password is Meta@123.<br>thank you"

            subject = "welcome,"
            msg = Message(recipients=[email],
                          html=message,
                          subject=subject)
            # mail.send(msg)
            thread1 = threading.Thread(target=mail.send(msg))
            thread1.start()
            send_data = {'success': True}
            return make_response(jsonify(send_data), 200)
    except Exception as e:
        print(str(e))
        send_data = {'success': False}
        return make_response(jsonify(send_data), 200)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))



@app.route('/Android/register', methods=['POST'])
def register1():
    try:
        if request.method == 'POST':
            first_name = '1'#request.form['first_name']
            email = '2'#request.form['email']
            phone = '3'#request.form['phone']
            password ='233' #generate_password_hash(request.form['password'])
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users (first_name, last_name,password, email, phone,created_at) "
                        "VALUES (%s, %s ,%s, %s,%s, %s ,%s, %s)",
                        (first_name, last_name, password, email, phone,datetime.datetime.now()))
            mysql.connection.commit()
            cur.close()
            # msg = Message('Welcome', recipients=[email])
            # thread1 = threading.Thread(target=mail.send(msg))
            # thread1.start()
            message = "hi,"+first_name+"<br>you have successfully created account on Metaorigin Labs.your username "+email+", password is Meta@123.<br>thank you"

            subject = "welcome,"
            msg = Message(recipients=[email],
                          html=message,
                          subject=subject)
            # mail.send(msg)
            thread1 = threading.Thread(target=mail.send(msg))
            thread1.start()
            send_data = {'success': True}
            return make_response(jsonify(send_data), 200)
    except Exception as e:
        print(str(e))
        send_data = {'success': False}
        return make_response(jsonify(send_data), 200)



@app.route('/damage_check', methods=['POST'])
def damage_check():
    try:
        if request.method == 'POST':
            user_id = request.form['user_id']
            if not user_id:
                user_id = 1

            file = request.files['fileUpload']
            if file and allowed_file(file.filename):
                uid = randomString(10)
                filename = file.filename
                ext = filename.split(".")[-1]
                name = filename.split(".")[:-1]
                file_name = name[0]+'_'+uid+'.'+ext
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
                orig_img = file_name
                learn = setup_learner()
                img = open_image(app.config['UPLOAD_FOLDER']+'/'+file_name)
                out_put = infer_imagewithcontours(img, learn)
                # print(out_put)
                ext = filename.split(".")[-1]
                name = filename.split(".")[:-1]
                file_name = name[0] + '_'+uid+'_' + '_final' + '.' + ext
                # img = open_image(app.config['UPLOAD_FOLDER']+'/'+file_name)
                permission_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)

                out_put = cv2.cvtColor(out_put*255, cv2.COLOR_BGR2RGB)
                cv2.imwrite(app.config['UPLOAD_FOLDER']+'/'+file_name, out_put)
                process_img = file_name

                print("***************")
                print(permission_path)
                subprocess.call(['chmod', 'a+rwx', permission_path])
                print("**************end*************")

                cur = mysql.connection.cursor()
                cur.execute(
                    "INSERT INTO images (user_id,original_img, process_img,created_at) "
                    "VALUES (%s, %s ,%s, %s)",
                    (user_id, orig_img, process_img, datetime.datetime.now()))
                mysql.connection.commit()
                cur.close()

            send_data = {'success': True, 'image': 'http://localhost:4000/file/'+file_name}
            return make_response(jsonify(send_data), 200)
    except Exception as e:
        print(str(e))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        send_data = {'success': False}
        return make_response(jsonify(send_data), 200)




def setup_learner():
    try:
        # learn = load_learner(app.config['MODEL_FOLDER'], 'scratch_detector.pkl')
        print("Entering setup learner!")
        path = app.config['MODEL_FOLDER']
        file = 'scratch_detector.pkl'
        test = None
        tfm_y=None
        source = Path(app.config['MODEL_FOLDER'])/'scratch_detector.pkl' if is_pathlike('scratch_detector.pkl') else 'scratch_detector.pkl'
        print("took up the source")
        state = torch.load(source, map_location='cpu') if defaults.device == torch.device('cpu') else torch.load(source)
        model = state.pop('model')
        src = LabelLists.load_state(path, state.pop('data'))
        if test is not None: src.add_test(test, tfm_y=tfm_y)
        data = src.databunch()
        cb_state = state.pop('cb_state')# **db_kwargs
        clas_func = state.pop('cls')
        res = clas_func(data, model, **state)
        res.callback_fns = state['callback_fns'] #to avoid duplicates
        res.callbacks = [load_callback(c,s, res) for c,s in cb_state.items()]
        return res
        # return learn
    except RuntimeError as e:
        if len(e.args) > 0 and 'CPU-only machine' in e.args[0]:
            print(e)
            message = "\n\nThis model was trained with an old version of fastai and will not work in a CPU environment.\n\nPlease update the fastai library in your training environment and export your model again.\n\nSee instructions for 'Returning to work' at https://course.fast.ai."
            raise RuntimeError(message)
        else:
            raise

            
def acc_cars(input, target):
  target = target.squeeze(1)
  return (input.argmax(dim=1)==target).float().mean()
def infer_imagewithcontours(img,learn):
    mask,_,_ = learn.predict(img)
    # erode_kernel = np.ones((3,3))
    mask_copy = mask.data
    np_mask = np.asarray(mask_copy).reshape(448, 448)
    # np_mask = cv2.erode(np.uint8(np_mask), erode_kernel, 1)
    cnts = cv2.findContours(np.uint8(np_mask), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    image_copy  = img.resize(448).data
    image_copy= np.asarray(image_copy)
    out= np.transpose(image_copy, (1, 2, 0))
    # for c in cnts:
    #   out = cv2.drawContours(out, [c], -1, (0, 255, 0), 2)
    out = coordinate_bbox_generator(cnts, out)
    # print(type(out))
    # alpha = 0.3
    # out = alpha * np_mask.reshape(448,448,1) + (1-alpha) * out.get()
    # return out
    return out

def doOverlap(l1, r1, l2, r2): 
    # If one rectangle is on doOverlap(l1, r1, l2, r2)left side of other 
    if(l1[0] > r2[0] or l2[0] > r1[0]): 
        return False
  
    # If one rectangle is above other   
    if(l1[1] > r2[1] or l2[1] > r1[1]): 
        return False
  
    return True

def overlap_handler(l1, r1, l2, r2):
  l3 = (min(l1[0], l2[0]), min(l1[1], l2[1]))
  r3 = (max(r1[0], r2[0]), max(r1[1], r2[1]))
  return l3, r3

# def coordinate_bbox_generator(cnt, img):
#     for box in cnt:
#         x_coord, y_coord = [], []
#         for item in box:
#             x_coord.append(item[0][0])
#             y_coord.append(item[0][1])
#         r = x_coord
#         c = y_coord
#         # print(img)
#         c1 = (int(min(r)), int(min(c)))
#         # print(c1)
#         c2 = (int(max(r)), int(max(c)))
#         # print(c1)
#         # print(c2)
#         if c2[0]-c1[0] > 3 and c2[1] - c1[1] > 3:
#             img = cv2.UMat(img).get()
#             img = cv2.rectangle(img, c1, c2, (255, 0, 0), 1)
#         # print(111111111)
#         # print(img)
#     return img



def coordinate_bbox_generator(cnt, img):
  filtered_box = []
  for box in cnt:
    x_coord, y_coord = [], []
    for item in box:
      # print(item)
      x_coord.append(item[0][0])
      y_coord.append(item[0][1])
      # print(x_coord)
    r = x_coord
    c = y_coord
    # print(img)
    c1 = (min(r), min(c))
    # print(c1)
    c2 = (max(r), max(c))
    # print(c2)
    if (c2[0]-c1[0]>3 and c2[1]-c1[1]>3):
      filtered_box.append([c1, c2])
      # img = cv2.rectangle(img, c1, c2, (0, 0, 255), 1)
  print(len(filtered_box))
  for idx1 in range(len(filtered_box)):
    final_box = filtered_box[idx1]
    # print(idx1)
    for idx2 in range(len(filtered_box)):
      # print(idx1, idx2)
      item1, item2 = filtered_box[idx1], filtered_box[idx2]
      # print(*item1, *item2)
      if idx1==idx2:
        continue
      elif doOverlap(*item1, *item2):
        # print("Yippee!!")
        filtered_box[idx2] = overlap_handler(*item1, *item2)
      # print(len(filtered_box))
  for item in filtered_box:
    img = cv2.UMat(img).get()
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.rectangle(img, *item, (255, 0, 0), 1)
  return img

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='4000')
