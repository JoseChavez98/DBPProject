from flask import Flask,render_template,session,request, jsonify, Response, url_for
import os
from flask import Flask,flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from model import entities
from database import connector
import json


app = Flask(__name__)
db = connector.Manager()

UPLOAD_FOLDER = '/static'
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOADED_FOLDER'] = 'static/'


cache = {}
engine = db.createEngine()

##############################################################################
##################### LOGS ##################################################
#############################################################################

@app.route('/')
def hello_world():
    return render_template('login.html')

@app.route('/logout',methods=['POST'])
def log_out():
    print('sali')
    return render_template('login.html')

@app.route('/dologin',  methods = ['POST'])
def do_login():

    data = request.form
    session = db.getSession(engine)
    users = session.query(entities.User)
    for user in users:
        print('\n')
        print(user.name)

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
        print("From DB")
    else:
        print("From Cache")

    users = cache[key];
    response = []
    for user in users:
        response.append(user)
    return json.dumps(response, cls=connector.AlchemyEncoder)

#@app.route('/users/<id>', methods = ['GET'])
#def get_user(id):
#    session = db.getSession(engine)
#    users = session.query(entities.User).filter(entities.User.id == id)
#    for user in users:
#        js = json.dumps(user, cls=connector.AlchemyEncoder)
#        return  Response(js, status=200, mimetype='application/json')

#    message = { "status": 404, "message": "Not Found"}
#    return Response(message, status=404, mimetype='application/json')


#@app.route('/users', methods = ['DELETE'])
#def remove_user():
#    id=request.form['key']
#    session = db.getSession(engine)
#    users = session.query(entities.User).filter(entities.User.id == id)
#    for user in users:
#        session.delete(user)
#    session.commit()
#    return "DELETED"


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
        print("entre al if")
        session.add(user)
        session.commit()
        print("\nagregado exitosamente")
        return render_template('login.html')
    else:
        print("no entre")
        return render_template('register.html')


@app.route('/users', methods = ['POST'])
def create_user():
    c = json.loads(request.form['values'])
    print("entre a users")
    print(c)
    user = entities.User(
        name=c['name'],
        email=c['fullname'],
        password=c['password']
    )

    session = db.getSession(engine)
    users = session.query(entities.User).filter(entities.User.name)
    emails = session.query(entities.User).filter(entities.User.email)
    if user.name not in users :
        print("entre al if")
        session.add(user)
        session.commit()
        print("\nagregado exitosamente")
        return render_template('login.html')
    else:
        print("no entre")
        return render_template('register.html')
#@app.route('/users', methods = ['PUT'])
#def update_user():
#    session = db.getSession(engine)
#    id = request.form['key']
#    user = session.query(entities.User).filter(entities.User.id == id).first()
#    c =  json.loads(request.form['values'])
#    for key in c.keys():
#        setattr(user, key, c[key])
#    session.add(user)
#    session.commit()
#    return ('Updated User')




##############################################################################
################## UPLOAD IMAGES #############################################
#############################################################################

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/showupload',methods=['POST'])
def show():
    return render_template('upload.html')

@app.route('/upload', methods=['GET','POST'])
def upload_file():

    file = request.files['image']
    f= os.path.join(app.config['UPLOADED_FOLDER'], file.filename)
    print(file.filename)
    im = entities.Image.path.info
    session1 = db.getSession(engine)
    session1.add(im)
    session1.commit()
    file.save(f)
    print("subida exitosa")

    return render_template('upload.html')


if __name__ == '__main__':
    app.run()
    #app.run(host='0.0.0.0', port=8080)

