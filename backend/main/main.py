from flask import Flask, jsonify, abort
from dataclasses import dataclass
import requests
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
import json
from producer import publish


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)




@dataclass
class Turf(db.Model):
    id: int
    title: str
    booked:int

    id=db.Column(db.Integer, primary_key = True, autoincrement=False)
    title = db.Column(db.String(200))
    booked = db.Column(db.Integer)

@dataclass
class TurfUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column (db.Integer)
    turf_id = db.Column(db.Integer)
    date=db.Column(db.String(200))
    date=db.Column(db.String(200))
    
    UniqueConstraint('user_id', 'turf_id', name='user_turf_unique')

@app.route('/api/turfs')
def index():
    return jsonify(Turf.query.all())


@app.route('/api/turfs/<int:id>/book',methods=['POST'])
def book(id):
    req = requests.get('http://host.docker.internal:8000/api/user')
    json=req.json()
    try:
        turfUser = TurfUser(user_id=json['id'],turf_id=id)
        db.session.add(turfUser)
        db.session.commit()
        
        publish('turf_booked',id)


    except:
        abort(400,'turf is already booked')
    
    return jsonify({
        "message" : "success"
    })



if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0')