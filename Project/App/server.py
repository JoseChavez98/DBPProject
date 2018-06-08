from flask import Flask,render_template,session,request, jsonify, Response, url_for
from model import entities
from database import connector
import json


app = Flask(__name__)
db = connector.Manager()

cache = {}
engine = db.createEngine()


@app.route('/images/<content>')
def images(content):
    return render_template(content)

#@app.route('/static/<content>')
#def static_content(content):
#    return render_template(content)


@app.route('/')
def hello_world():
    return render_template('login.html')

@app.route('/dologin',  methods = ['POST'])
def do_login():

    data = request.form
    session = db.getSession(engine)
    users = session.query(entities.User)
    for user in users:
        print('\n')
        print(user.name)

        if user.name == data['username'] and user.password == data['password']:
            return render_template('home.html')

    return render_template('login.html')




@app.route('/setUsers')
def set_user():

    user1 = entities.User(id=1, name='jose', fullname='jose chavez', password='1234')
    user2 = entities.User(id=2, name='guille', fullname='guillermo', password='1234')
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

@app.route('/users/<id>', methods = ['GET'])
def get_user(id):
    session = db.getSession(engine)
    users = session.query(entities.User).filter(entities.User.id == id)
    for user in users:
        js = json.dumps(user, cls=connector.AlchemyEncoder)
        return  Response(js, status=200, mimetype='application/json')

    message = { "status": 404, "message": "Not Found"}
    return Response(message, status=404, mimetype='application/json')


@app.route('/users', methods = ['DELETE'])
def remove_user():
    id=request.form['key']
    session = db.getSession(engine)
    users = session.query(entities.User).filter(entities.User.id == id)
    for user in users:
        session.delete(user)
    session.commit()
    return "DELETED"


@app.route('/users', methods = ['POST'])
def create_user():
    c = json.loads(request.form['values'])
    print(c)
    user = entities.User(
        id=c['id'],
        name=c['name'],
        fullname=c['fullname'],
        password=c['password']
    )
    session = db.getSession(engine)
    session.add(user)
    session.commit()
    return 'Created users'
@app.route('/users', methods = ['PUT'])
def update_user():
    session = db.getSession(engine)
    id = request.form['key']
    user = session.query(entities.User).filter(entities.User.id == id).first()
    c =  json.loads(request.form['values'])
    for key in c.keys():
        setattr(user, key, c[key])
    session.add(user)
    session.commit()
    return ('Updated User')

if __name__ == '__main__':
    app.run()

