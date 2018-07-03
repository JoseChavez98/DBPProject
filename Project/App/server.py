from flask import Flask,render_template,session,request, jsonify, Response
import os
from flask import Flask,flash, request, redirect, url_for
from sqlalchemy import or_, and_
from model import entities
from database import connector
import json


app = Flask(__name__)
db = connector.Manager()

UPLOAD_FOLDER = '/static'
extensions=[ 'png', 'jpg', 'jpeg', 'gif']

app.config['UPLOADED_FOLDER'] = 'static/'


cache = {}
engine = db.createEngine()
username = ""
def name_user(a):
    global username
    username=a


##############################################################################
##################### LOGS ##################################################
#############################################################################

@app.route('/')
def hello_world():
    return render_template('login.html')

@app.route('/logout',methods=['POST'])
def log_out():
    return render_template('login.html')

@app.route('/dologin',  methods = ['POST'])
def do_login():

    data = request.form
    session = db.getSession(engine)
    users = session.query(entities.User)
    for user in users:
        if (user.name == data['username'] or user.email == data['username']) and user.password == data['password']:
            return render_template('home.html')

    return render_template('login.html')

@app.route('/showsignup',methods=['POST'])
def show_signup():
    return render_template('register.html')

@app.route('/showlogin',methods=['POST'])
def show_login():
    return render_template('login.html')

@app.route('/showhome',methods=['POST'])
def show_home():
    return render_template('home.html')

@app.route('/mobile_login', methods = ['POST'])
def mobile_login():
    obj = request.get_json(silent=True)
    print(obj)
    username = obj['username']
    password = obj['password']
    sessiondb = db.getSession(engine)
    user = sessiondb.query(entities.User).filter(
        and_(entities.User.name == username, entities.User.password == password )
    ).first()
    if user != None:
        #session['logged'] = user.id;
        return Response(json.dumps({'response': True}, cls=connector.AlchemyEncoder), mimetype='application/json')
    else:
        return Response(json.dumps({'response': False}, cls=connector.AlchemyEncoder), mimetype='application/json')
##############################################################################
################# USERS ######################################################
##############################################################################


@app.route('/setUsers')
def set_user():

    user1 = entities.User( name='jose', email='jose.chavez@utec.edu.pe', password='1234')
    user2 = entities.User( name='guille', email='guillermo.franco@utec.edu.pe', password='1234')
    session = db.getSession(engine)
    session.add(user1)
    session.add(user2)

    session.commit()
    return 'Created users'


@app.route('/users', methods = ['GET'])
def get_users():
    key = 'getUsers'
    if key not in cache.keys():
        session = db.getSession(engine)
        dbResponse = session.query(entities.User)
        cache[key] = dbResponse;



    users = cache[key];
    response = []
    for user in users:
        response.append(user)
    return json.dumps(response, cls=connector.AlchemyEncoder)



@app.route('/register', methods = ['POST'])
def register():
    user = entities.User(
        name=request.form['username'],
        email=request.form['email'],
        password=request.form['password']
    )
    session = db.getSession(engine)
    users = session.query(entities.User).filter(entities.User.name)
    emails = session.query(entities.User).filter(entities.User.email)
    if user.name not in users and user.email not in emails:

        session.add(user)
        session.commit()
        return render_template('login.html')
    else:
        return render_template('register.html')


@app.route('/users', methods = ['POST'])
def create_user():
    c = json.loads(request.form['values'])
    user = entities.User(
        name=c['name'],
        email=c['fullname'],
        password=c['password']
    )

    session = db.getSession(engine)
    users = session.query(entities.User).filter(entities.User.name)
    emails = session.query(entities.User).filter(entities.User.email)
    if user.name not in users :
        session.add(user)
        session.commit()
        return render_template('login.html')
    else:
        return render_template('register.html')





##############################################################################
################## UPLOAD IMAGES #############################################
#############################################################################


@app.route('/showupload',methods=['POST'])
def show():
    return render_template('upload.html')

@app.route('/upload', methods=['GET','POST'])

def upload_file():

    file = request.files['image']
    cast=file.filename.split('.')
    if(cast[1] in extensions):
        f= os.path.join(app.config['UPLOADED_FOLDER'], file.filename)
        im = entities.Image()
        im.path = file.filename

        im.likes = 0
        session1 = db.getSession(engine)
        session1.add(im)
        session1.commit()
        file.save(f)

        return render_template('upload.html')
    else:
        return render_template('upload.html')

@app.route('/images', methods = ['GET'])
def get_images():

    session = db.getSession(engine)
    images = session.query(entities.Image)

    response = []
    for image in images:
        response.append(image)
    return json.dumps(response, cls=connector.AlchemyEncoder)


if __name__ == '__main__':
    app.run()
    #app.run(host='0.0.0.0', port=8080)

